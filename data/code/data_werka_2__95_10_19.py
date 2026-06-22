class Validator:
    def combine_and_report(self, a, b, c):
        results = []
        if a <= 0:
            results.append(f"{a} is not positive")
        elif a % 2 != 0:
            results.append(f"{a} is odd")
        elif a >= 100:
            results.append(f"{a} is too large")
        else:
            results.append(f"{a} is valid")

        if b <= 0:
            results.append(f"{b} is not positive")
        elif b % 2 != 0:
            results.append(f"{b} is odd")
        elif b >= 100:
            results.append(f"{b} is too large")
        else:
            results.append(f"{b} is valid")

        if c <= 0:
            results.append(f"{c} is not positive")
        elif c % 2 != 0:
            results.append(f"{c} is odd")
        elif c >= 100:
            results.append(f"{c} is too large")
        else:
            results.append(f"{c} is valid")

        combined = a + b + c
        return {
            "inputs": [a, b, c],
            "sum": combined,
            "reports": results
        }

if __name__ == '__main__':
    v = Validator()
    print(v.combine_and_report(10, 25, -5))