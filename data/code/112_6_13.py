class SimpleAdder:
    def add(self, a, b):
        try:
            return int(a) + int(b)
        except ValueError:
            raise ValueError("Error: Both inputs must be convertible to integers.")

if __name__ == '__main__':
    calculator = SimpleAdder()
    print(calculator.add(5, 10))
    print(calculator.add("5", "10"))
    try:
        print(calculator.add(3.5, 7))
    except ValueError as e:
        print(e)