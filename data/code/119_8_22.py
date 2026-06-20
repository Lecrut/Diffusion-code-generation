class IntegerSwapper:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def swap(self):
        temp = self.x
        self.x = self.y
        self.y = temp

if __name__ == '__main__':
    manager = IntegerSwapper(5, 10)
    manager.swap()
    print(f"Swapped values: x={manager.x}, y={manager.y}")