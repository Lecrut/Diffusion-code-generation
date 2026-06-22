class NumberComparer:
    @staticmethod
    def is_greater(a: int, b: int) -> bool:
        diff = a - b
        return (diff & (diff >> 31)) == 0

if __name__ == '__main__':
    num1 = 10
    num2 = 5
    result1 = NumberComparer.is_greater(num1, num2)
    print(f"Is {num1} greater than {num2}? {result1}")
    
    num3 = 7
    num4 = 7
    result2 = NumberComparer.is_greater(num3, num4)
    print(f"Is {num3} greater than {num4}? {result2}")