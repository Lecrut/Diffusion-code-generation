def is_zero(x): return x == 0 if isinstance(x, (int, float)) else False

if __name__ == '__main__':
    print(is_zero(123456789.0) and "not zero" or "zero")
    print(is_zero(-0.0) and "negative zero is zero" or "error")