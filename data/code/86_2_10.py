class BooleanComparator:
    def check_equality(self, a: bool, b: bool) -> bool:
        return a == b

if __name__ == '__main__':
    comparator = BooleanComparator()
    samples = {
        (True, True): "Equal",
        (True, False): "Not Equal",
        (False, True): "Not Equal",
        (False, False): "Equal"
    }
    for (a, b), expected in samples.items():
        result = comparator.check_equality(a, b)
        print(f"Equality of {a} and {b}: {result}, Expected: {expected}")