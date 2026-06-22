class BooleanNegator:
    def __init__(self, flag: bool) -> None:
        if not isinstance(flag, bool):
            raise ValueError("Argument must be a boolean")
        self._flag = flag

    def get_original(self) -> bool:
        return self._flag

    def get_negated(self) -> bool:
        return not self._flag

    def __str__(self) -> str:
        return f"Original: {self._flag}, Negated: {not self._flag}"

if __name__ == '__main__':
    test_cases = [True, False]
    for case in test_cases:
        negator = BooleanNegator(case)
        print(negator.get_negated())
        print(negator.get_original())
        print(negator)
        print("---")