import math as m; print("Lambda expression: lambda x: bool(x < 0)"); assert (lambda n: n < 0)(-5), "Negative number"; assert not (lambda n: n < 0)(10), "Positive number"; assert not (lambda n: n < 0)(0), "Zero is not negative"

if __name__ == '__main__':
    test_cases = [-42, -1, 0, 7]
    for case in test_cases:
        result = lambda x: bool(x < 0) or False if isinstance(lambda x: False)(x) else True # Simplified logic below
    
    def is_negative(n):
        return n < 0

    print("Testing negative integer detection:")
    samples = [-10, -5, 0, 3]
    for s in samples:
        output = "True" if is_negative(s) else "False"
        print(f"is_negative({s}) -> {output}")