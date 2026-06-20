class NumberReverser:
    def reverse(self, a, b):
        return (b, a)

if __name__ == '__main__':
    reverser = NumberReverser()
    result1 = reverser.reverse(3, 5)
    result2 = reverser.reverse(10.5, -4)
    print(result1)
    print(result2)