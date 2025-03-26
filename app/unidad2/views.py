from flask import Flask, request, render_template
from . import unidad2 
import time

@unidad2.route('/biseccion', methods=['GET', 'POST'])
def biseccion():
    keyboard_content = render_template('KeyboardMath.html', time=time.time())
    print('entro')
    if request.method == 'POST':
        # Obtener datos del formulario
        a = float(request.form['a'])
        b = float(request.form['b'])
        tol = float(request.form['tol'])
        
        # Aquí puedes agregar tu lógica del método de bisección
        resultado = f"Valores recibidos - a: {a}, b: {b}, tolerancia: {tol}"
        
        return resultado  # Devuelve respuesta al cliente
    
    return render_template('unidad2/biseccion.html', keyboard_content=keyboard_content, time=time.time())  # Renderiza el formulario si es GET

@unidad2.route('/pruebarender', methods=['GET'])
def pruebarender():
     # Datos que se pasarán a la plantilla
    datos = {
        'titulo': 'Bienvenido a mi página web',
        'mensaje': 'Esta es una página generada con Flask y Jinja2.',
        'navegacion': [
            {'href': '/', 'caption': 'Inicio'},
            {'href': '/acerca-de', 'caption': 'Acerca de'},
            {'href': '/contacto', 'caption': 'Contacto'}
        ]
    }
    # Renderizar la plantilla con los datos
    return render_template('pruebarender.html', **datos)