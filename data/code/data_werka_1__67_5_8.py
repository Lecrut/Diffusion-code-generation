class NumberAdder:
    def __init__(self):
        self.result = None

    @staticmethod
    def add_numbers(a, b):
        try:
            result = float(a) + float(b)
            return result
        except ValueError:
            raise ValueError("Both inputs must be numbers")

if __name__ == '__main__':
    adder = NumberAdder()
    print(adder.add_numbers(5, 10))
    print(adder.add_numbers(20.5, 22.3))
    try:
        print(adder.add_numbers('a', 10))
    except ValueError as e:
        print(e)