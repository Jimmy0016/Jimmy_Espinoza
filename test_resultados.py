"""Pruebas para la calculadora."""
from app import sumar, restar

def test_sumar():
    """Prueba la función de sumar."""
    assert sumar(2, 3) == 5
    assert sumar(-1, 1) == 0

def test_restar():
    """Prueba la función de restar."""
    assert restar(5, 2) == 3
    assert restar(0, 4) == -4

def test_sumar_y_restar():
    """Prueba la integración de sumar y restar."""
    resultado = restar(sumar(2, 3), 1)
    assert resultado == 4

def test_operacion_combinada_negativa():
    """Prueba la integración con negativos."""
    resultado = restar(sumar(-5, 2), 4)
    assert resultado == -7
    
    

# <-- ASEGÚRATE DE DEJAR UNA LÍNEA VACÍA AQUÍ AL FINAL DEL ARCHIVO