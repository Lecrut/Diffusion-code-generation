class FloatReverser:
    def reverse(self, a: float, b: float) -> (float, float):
        return b, a

if __name__ == '__main__':
    reverser = FloatReverser()
    result = reverser.reverse(3.14, 2.71)
    print(result)