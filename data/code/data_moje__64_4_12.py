def power(base, exp):
    if exp == 0:
        return 1
    if exp < 0:
        return 1 / power(base, -exp)
    
    def _pow(b, e):
        if e == 0:
            return 1
        h = _pow(b, e // 2)
        if e % 2 == 0:
            return h * h
        return h * h * b
    
    if exp > 30:
        import math
        if base == 0:
            return 0
        if base == 1:
            return 1
        if base == -1:
            return 1 if exp % 2 == 0 else -1
        log_val = exp * math.log10(abs(base))
        if log_val > 308:
            return float('inf') if (base > 0 or exp % 2 == 0) else float('-inf')
        if log_val < -308:
            return 0
        result = 10 ** (log_val - math.floor(log_val))
        exponent = 10 ** math.floor(log_val)
        return result * exponent
    return _pow(base, exp)

if __name__ == '__main__':
    print(power(2, 10))
    print(power(2, 100))
    print(power(3, 0))
    print(power(2, -2))
    print(power(5, 50))