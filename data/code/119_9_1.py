class Reverser:
    def __init__(self, a, b):
        self._a = a
        self._b = b
    def reverse_attributes(self):
        temp = self._a
        self._a = self._b
        self._b = temp
if __name__ == '__main__':
    original_a = 10
    original_b = 20
    obj = Reverser(original_a, original_b)
    print(f"Before reversal: a={obj._a}, b={obj._b}")
    obj.reverse_attributes()
    print(f"After reversal: a={obj._a}, b={obj._b}")