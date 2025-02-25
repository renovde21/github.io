import pandas as pd
import pyodbc

# Connection parameters
server = 'localhost'  # Vervang door jouw servernaam
database = 'data_warehouse'                   # Vervang door je database
username = 'SA'             # SQL Server-gebruiker
password = 'Letmein!'                 # Wachtwoord
driver = '{ODBC Driver 17 for SQL Server}'   # Zorg dat je dit hebt geïnstalleerd
connection_string = 'DRIVER={ODBC Driver 17 for SQL Server};SERVER=localhost;DATABASE=data_warehouse;UID=SA;PWD=Letmein!;Encrypt=Yes;TrustServerCertificate=yes;Connection Timeout=30;'


# Maak connectie
try:
    conn = pyodbc.connect(f'DRIVER={driver};SERVER={server};DATABASE={database};UID={username};PWD={password};')
    #conn = pyodbc.connect(connection_string)
    print("Verbinding geslaagd!")
    cursor = conn.cursor()
    # Voorbeeldquery uitvoeren
    cursor.execute("SELECT TOP 10 * FROM DimDate")  # Pas de tabelnaam aan
    for row in cursor.fetchall():
        print(row)

except pyodbc.OperationalError as e:
    print(f"Operationele fout: {e}")
except pyodbc.DatabaseError as e:
    print(f"Database fout: {e}")
except pyodbc.Error as e:
    print(f"Algemene SQL fout: {e}")
except Exception as e:
    print(f"Algemene fout: {e}")
finally:
        cursor.close()
        conn.close()