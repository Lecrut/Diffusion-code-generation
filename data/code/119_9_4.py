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
    obj = Reverser(10, 20)
    print(f"Original: obj._a={obj._a}, obj._b={obj._b}")
    obj.reverse()
    print(f"Reversed: obj._a={obj._a}, obj._b={obj._b}")
    obj2 = Reverser(5, 8)
    print(f"Original: obj2._a={obj2._a}, obj2._b={obj2._b}")
    obj2.reverse()
    print(f"Reversed: obj2._a={obj2._a}, obj2._b={obj2._b}")