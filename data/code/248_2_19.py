class IntegerAdder:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

    def sum(self) -> int:
        return self.x + self.y

if __name__ == '__main__':
    adder_instance = IntegerAdder(10, 20)
    print("Sum:", adder_instance.sum())