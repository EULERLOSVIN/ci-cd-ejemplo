# test_calculadora.py
from calculadora import suma, resta, multiplicacion, division
import pytest

def test_suma():
    assert suma(2, 3) == 5

def test_resta():
    assert resta(5, 2) == 3

def test_multiplicacion():
    assert multiplicacion(4, 5) == 20

def test_division():
    assert division(10, 2) == 5

def test_division_por_cero():
    with pytest.raises(ValueError):
        division(5, 0)
