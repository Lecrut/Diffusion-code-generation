class BooleanComparator:
    def check_equality(self, a: bool, b: bool) -> bool:
        return a == b

if __name__ == '__main__':
    comparator = BooleanComparator()
    sample_values = {
        (True, True): "Equal",
        (True, False): "Not Equal",
        (False, True): "Not Equal",
        (False, False): "Equal"
    }
    
    for (a, b), expected in sample_values.items():
        result = comparator.check_equality(a, b)
        print(f"Equality of {a} and {b}: {result}, Expected: {expected}")