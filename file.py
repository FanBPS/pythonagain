import zipfile
zip = zipfile.ZipFile('compfiles.zip', 'w')
zip.write('blackpinea.png')
zip.close()

import firebase_admin
from firebase_admin import credentials

cred = credentials.Certificate("C:\\Users\\youri\\Downloads\\pythonproject-71d63-firebase-adminsdk-95ooh-afc6f84041.json")
firebase_admin.initialize_app(cred)
