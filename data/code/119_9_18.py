class IntegerReverser:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def reverse(self):
        self.x, self.y = self.y, self.x

if __name__ == '__main__':
    original_x = 10
    original_y = 20
    reverser = IntegerReverser(original_x, original_y)
    print(f"Before reversal: x={reverser.x}, y={reverser.y}")
    reverser.reverse()
    print(f"After reversal: x={reverser.x}, y={reverser.y}")