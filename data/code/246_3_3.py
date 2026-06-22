class LargeIntCalculator:
    def add(self, a: int, b: int) -> int:
        return a + b

if __name__ == '__main__':
    calc = LargeIntCalculator()
    result1 = calc.add(5, 3)
    print(result1)
    
    num1 = 98765432109876543210
    num2 = 12345678901234567890
    result2 = calc.add(num1, num2)
    print(result2)