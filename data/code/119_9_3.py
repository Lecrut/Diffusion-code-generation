class Reverser:
    def __init__(self, a, b):
        self._a = a
        self._b = b
    def reverse_attributes(self):
        temp = self._a
        self._a = self._b
        self._b = temp
if __name__ == '__main__':
    obj = Reverser(10, 20)
    print(f"Before: a={obj._a}, b={obj._b}")
    obj.reverse_attributes()
    print(f"After: a={obj._a}, b={obj._b}")
    obj2 = Reverser(5, 8)
    print(f"Before: a={obj2._a}, b={obj2._b}")
    obj2.reverse_attributes()
    print(f"After: a={obj2._a}, b={obj2._b}")