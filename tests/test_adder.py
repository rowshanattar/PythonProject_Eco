
from main import adder

def test_adder():
    assert adder(2, 3) == 5
    assert adder(-1, 1) == 0
    assert adder(0, 0) == 0