from thingerio import ThingerDevice

# Benutzerdefinierte Konfiguration für Thinger.io
THINGER_USERNAME = 'Khaled91'
DEVICE_ID = '123456mkmk'
DEVICE_CREDENTIALS = '123456mkmk'  # Die Geräteanmeldeinformationen

# Verbindung zum Thinger.io-Dienst herstellen
thinger = ThingerDevice(THINGER_USERNAME, DEVICE_ID, DEVICE_CREDENTIALS)

# Testdaten für den Upload an Thinger.io
test_data = [
    {'sensor': 'Temperatursensor', 'value': 25.5},
    {'sensor': 'Luftfeuchtigkeitssensor', 'value': 60.0}
]

# Funktion zum Hochladen von Daten an Thinger.io
def upload_data_to_thinger(data):
    for sensor_data in data:
        thinger.handle('data', sensor_data)

if __name__ == '__main__':
    # Testdaten an Thinger.io senden
    upload_data_to_thinger(test_data)
