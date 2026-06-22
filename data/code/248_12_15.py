class Adder:
    @staticmethod
    def validate_number(value):
        if not isinstance(value, (int, float)):
            raise TypeError("Both inputs must be numbers")

    @classmethod
    def add(cls, a: int, b: int) -> int:
        cls.validate_number(a)
        cls.validate_number(b)
        return a + b

if __name__ == '__main__':
    result = Adder.add(3, 5)
    print(result)