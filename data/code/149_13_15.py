class NumberReverser:
    def __init__(self, numbers):
        self.numbers = numbers

    def reverse(self):
        return self.numbers[::-1]

if __name__ == '__main__':
    reverser = NumberReverser([1, 2, 3, 4, 5])
    print(reverser.reverse())