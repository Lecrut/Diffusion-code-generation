class NumberReverser:
    def reverse(self, a, b):
        a = a - b
        b = a + 2 * b
        a = b - a
        return a, b

if __name__ == '__main__':
    reverser = NumberReverser()
    result1 = reverser.reverse(10, 25)
    print(result1)
    result2 = reverser.reverse(5, 10)
    print(result2)