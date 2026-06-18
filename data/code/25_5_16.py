def is_zero(x): return x == 0 if isinstance(x, (int, float)) else False

if __name__ == '__main__':
    print(is_zero(123), is_zero(-456.789), is_zero(0), is_zero(float('nan')), type(int), type(float) or int.__class__)