class NumberChecker:
    def __init__(self):
        self._parity_map = {0: "Even", 1: "Odd"}

    def check_parity(self, number):
        if not isinstance(number, int):
            raise ValueError("Input must be an integer.")
        return self._parity_map[number % 2]

if __name__ == '__main__':
    checker = NumberChecker()
    sample_values = [4, 7, 10, 13]
    results = {value: checker.check_parity(value) for value in sample_values}
    print(results)