class FloatReverser:
    @staticmethod
    def reverse_args(a: float, b: float) -> (float, float):
        return b, a

if __name__ == '__main__':
    original_values = (3.14, 2.71)
    reversed_values = FloatReverser.reverse_args(*original_values)
    print(reversed_values)