class NumberChecker:
    def __init__(self, value):
        self.value = value
    
    def check_greater(self, other):
        return self.value > other.value

if __name__ == '__main__':
    num1 = NumberChecker(50)
    num2 = NumberChecker(30)
    
    result = num1.check_greater(num2)
    print(f"{num1.value} is greater than {num2.value}: {result}")