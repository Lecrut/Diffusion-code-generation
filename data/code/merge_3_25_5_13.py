import math; zero_check = lambda x: abs(x) < 1e-9 if isinstance(x, (int, float)) else False

if __name__ == '__main__':
    print(zero_check(0))      # True
    print(zero_check(-0.0001))# False
    print(zero_check(float('inf')))   # False