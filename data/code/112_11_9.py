class NumberAdder:
    @staticmethod
    def add_two_numbers(a: float, b: float) -> float:
        return a + b

if __name__ == '__main__':
    result = NumberAdder.add_two_numbers(7.2, 3.8)
    print(result)