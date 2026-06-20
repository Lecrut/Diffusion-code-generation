class Reverser:
    def __init__(self, a, b):
        self._a = a
        self._b = b

    @staticmethod
    def reverse(a, b):
        return b, a

if __name__ == '__main__':
    original_a = 10
    original_b = 20
    new_a, new_b = Reverser.reverse(original_a, original_b)
    print(f"After reversal: a={new_a}, b={new_b}")