class SwapManager:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def swap(self):
        temp = self.x
        self.x = self.y
        self.y = temp

if __name__ == '__main__':
    manager1 = SwapManager(5, 10)
    manager2 = SwapManager(3, 8)

    manager1.swap()
    manager2.swap()

    print(f"Swapped values: x={manager1.x}, y={manager1.y}")
    print(f"Swapped values: a={manager2.x}, b={manager2.y}")