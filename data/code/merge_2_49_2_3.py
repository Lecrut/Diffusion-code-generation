import functools
class NumericValidator:
    def __init__(self):
        self._cache = None
    @functools.lru_cache(maxsize=128)
    def has_positive(self, numbers_tuple):
        return any(n > 0 for n in numbers_tuple)
def main():
    validator = NumericValidator()
    test_cases = [
        (5,),
        (-3, -7),
        (0, 1, -2),
        (),
        (float('inf'), float('-inf')),
    ]
    for case in test_cases:
        result = validator.has_positive(tuple(case))
        print(f"Input: {case}, Has positive number: {result}")
if __name__ == '__main__':
    main()