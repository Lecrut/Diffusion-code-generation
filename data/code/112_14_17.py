class DecimalAdder:
    @staticmethod
    def add(a, b):
        if not (isinstance(a, (int, float)) and isinstance(b, (int, float))):
            raise ValueError("Both inputs must be numbers")
        return a + b

if __name__ == '__main__':
    result = DecimalAdder.add(3.5, 2.7)
    print(result)