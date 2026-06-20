class NumberReverser:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def reverse(self):
        while self.x != 0:
            temp = self.x
            self.x = self.y - (self.y // self.x) * self.x
            self.y = temp
        return self.y

if __name__ == '__main__':
    reverser = NumberReverser(123456789, 987654321)
    result = reverser.reverse()
    print(f"Reversed number: {result}")