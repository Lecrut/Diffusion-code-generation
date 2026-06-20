class NumberSwapper:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def swap(self):
        temp = self.x
        self.x = self.y
        self.y = temp

if __name__ == '__main__':
    swapper = NumberSwapper(7, 2)
    swapper.swap()
    print(f"Swapped values: x={swapper.x}, y={swapper.y}")