import pytest
import sys
sys.path.append('.')
from examples.maths import Calc

def test_square():
    assert Calc.square(9) == 81