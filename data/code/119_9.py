class Reverser:
    def __init__(self, a, b):
        self._a = a
        self._b = b
    def reverse(self):
        new_a = self._b
        new_b = self._a
        self._a = new_a
        self._b = new_b
if __name__ == '__main__':
    original_a = 10
    original_b = 20
    reverser = Reverser(original_a, original_b)
    print(f"Before reversal: a={reverser._a}, b={reverser._b}")
    reverser.reverse()
    print(f"After reversal: a={reverser._a}, b={reverser._b}")