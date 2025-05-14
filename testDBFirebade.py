

import firebase_admin 
from firebase_admin import credentials, db

# Configura el acceso a Firebase
#cred = credentials.Certificate("testpoo-59c96.json")  # Cambia por el nombre del archivo JSON
cred = credentials.Certificate("testvscode-5996d.json")  # Cambia por el nombre del archivo JSON
firebase_admin.initialize_app(cred, {
    #"databaseURL": "https://testpoo-59c96-default-rtdb.firebaseio.com"  # Cambia con tu URL de la base de datos
    "databaseURL": "https://testvscode-5996d-default-rtdb.firebaseio.com/"  # Cambia con tu URL de la base de datos
})

# Referencia al nodo en la base de datos
ref = db.reference("nodo1")  # Cambia "nodo_principal" por tu ruta

# Escribe datos en tiempo real
ref.set({
    "mensaje": "Hola desde Python",
    "activo": True
})

# Escucha cambios en tiempo real
def escuchar_eventos(event):
    print(f"Cambio detectado: {event.data}")

ref.listen(escuchar_eventos)
