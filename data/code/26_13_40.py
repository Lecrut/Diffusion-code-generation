class IntegerComparison:
    @staticmethod
    def compare(a, b):
        if not isinstance(a, int) or not isinstance(b, int):
            raise ValueError("Both arguments must be integers.")
        return a > b

if __name__ == '__main__':
    try:
        result = IntegerComparison.compare(25, 10)
        print(result)
    except ValueError as e:
        print(e)