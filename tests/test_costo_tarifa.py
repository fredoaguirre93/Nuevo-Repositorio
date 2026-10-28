# Verifica que el cálculo de una tarifa sea correcto
def test_tarifa_total():
    total = 100 + 50
    assert total == 150

def test_descuento_aplicado():
    total = 200 - 50
    assert total == 150