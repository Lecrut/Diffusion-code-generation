class NumberReverser:
    def reverse(self, a, b):
        return (b, a)

if __name__ == '__main__':
    reverser = NumberReverser()
    result = reverser.reverse(10, 20)
    print(result)