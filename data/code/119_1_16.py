class NumberReverser:

    def reverse(self, a, b):
        if a > b:
            return (a, b)
        else:
            return (b, a)
if __name__ == '__main__':
    reverser = NumberReverser()
    result1 = reverser.reverse(10, 5)
    print(result1)
    result2 = reverser.reverse(-3, -8)
    print(result2)
    result3 = reverser.reverse(42, 42)
    print(result3)