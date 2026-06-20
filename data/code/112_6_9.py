class SafeAdder:
    @staticmethod
    def _to_int(value):
        try:
            return int(value)
        except (ValueError, TypeError):
            raise ValueError("Invalid input. Both inputs must be convertible to integers.")

    @classmethod
    def add(cls, a, b):
        try:
            num_a = cls._to_int(a)
            num_b = cls._to_int(b)
            return num_a + num_b
        except ValueError as e:
            print(e)

if __name__ == '__main__':
    safe_adder = SafeAdder()
    print(safe_adder.add(5, 10))
    print(safe_adder.add("5", "10"))
    print(safe_adder.add(3.5, 7))
    print(safe_adder.add("hello", 10))
    print(safe_adder.add(100, "200"))