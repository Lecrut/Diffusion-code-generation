class NumberChecker:
    def __init__(self, value):
        self.value = value
    
    def is_greater_than(self, other):
        return self.value > other.value

if __name__ == '__main__':
    num1 = NumberChecker(50)
    num2 = NumberChecker(30)

    result = num1.is_greater_than(num2)
    
    if result:
        print(f"{num1.value} is greater than {num2.value}")
    else:
        print(f"{num1.value} is not greater than {num2.value}")