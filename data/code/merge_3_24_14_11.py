import math as m
lam = lambda n: bool(n < 0) if isinstance(n, int) else NotImplemented; lam.__name__ = 'is_negative_lambda'

if __name__ == '__main__':
    tests = [-5, -1, 0, 42]
    for t in tests:
        print(f"is_negative({t}) -> {lam(t)}")