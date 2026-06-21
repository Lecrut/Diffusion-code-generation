class ZeroChecker:
    def __init__(self, value):
        if not isinstance(value, (int, float)):
            raise ValueError("Input must be an integer or a float")
        self.value = value

    def is_zero(self):
        return self.value == 0

if __name__ == '__main__':
    sample_values = [0, 1, -1, 2.5, None, '0', [], {}]
    results = {x: ZeroChecker(x).is_zero() if isinstance(x, (int, float)) else False for x in sample_values}
    print(results)