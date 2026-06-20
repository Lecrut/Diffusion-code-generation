class SimpleMath:
    def add(self, x: int, y: int) -> int:
        return x + y

    def subtract(self, x: int, y: int) -> int:
        return x - y

if __name__ == '__main__':
    math_instance = SimpleMath()
    print(math_instance.add(10, 5))
    print(math_instance.subtract(20, 8))