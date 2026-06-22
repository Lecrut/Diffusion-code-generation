class NumericOperations:
    @staticmethod
    def add(a: int, b: int) -> int:
        if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
            raise TypeError("Both inputs must be numbers")
        return a + b

if __name__ == '__main__':
    calc = NumericOperations()
    result1 = calc.add(3, 5)
    result2 = calc.add(7, 9)
    print(result1)
    print(result2)