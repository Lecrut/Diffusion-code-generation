class Validator:
    def combine_and_report(self, a, b, c):
        results = []
        if a <= 0:
            results.append(f"a={a} is not positive")
        elif a % 2 != 0:
            results.append(f"a={a} is odd")
        elif a >= 100:
            results.append(f"a={a} is not less than 100")
        else:
            results.append(f"a={a} is valid")

        if b <= 0:
            results.append(f"b={b} is not positive")
        elif b % 2 != 0:
            results.append(f"b={b} is odd")
        elif b >= 100:
            results.append(f"b={b} is not less than 100")
        else:
            results.append(f"b={b} is valid")

        if c <= 0:
            results.append(f"c={c} is not positive")
        elif c % 2 != 0:
            results.append(f"c={c} is odd")
        elif c >= 100:
            results.append(f"c={c} is not less than 100")
        else:
            results.append(f"c={c} is valid")

        combined = a + b + c
        return {
            'inputs': [a, b, c],
            'sum': combined,
            'status': results
        }

if __name__ == '__main__':
    validator = Validator()
    result = validator.combine_and_report(10, 25, -5)
    print(result)