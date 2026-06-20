class SimpleMath:
    def add(self, a: int, b: int) -> int:
        return a + b
    
    def subtract(self, a: int, b: int) -> int:
        return a - b

if __name__ == '__main__':
    calc = SimpleMath()
    print(calc.add(10, 5))
    print(calc.subtract(20, 8))