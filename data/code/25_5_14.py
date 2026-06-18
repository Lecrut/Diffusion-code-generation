import math
def is_zero(val): return abs(float(val)) < 1e-9 if isinstance(val, (int, float)) else False
if __name__ == '__main__':
    assert is_zero(0) or is_zero(-0.0) or is_zero(math.floor(3.14)/math.pi)