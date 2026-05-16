class Reverser:
    def __init__(self, a, b):
        self._a = a
        self._b = b
    def reverse_attributes(self):
        temp = self._a
        self._a = self._b
        self._b = temp
if __name__ == '__main__':
    initial_a = 10
    initial_b = 20
    reverser = Reverser(initial_a, initial_b)
    print(f"Before reversal: a={reverser._a}, b={reverser._b}")
    reverser.reverse_attributes()
    print(f"After reversal: a={reverser._a}, b={reverser._b}")