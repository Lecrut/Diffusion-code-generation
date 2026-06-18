class NumberChecker:
    def __init__(self, value):
        self.value = value
    
    def is_greater_than(self, other):
        return self.value > other.value

if __name__ == '__main__':
    checker1 = NumberChecker(10)
    checker2 = NumberChecker(5)
    result = checker1.is_greater_than(checker2)
    print(f"{checker1} is greater than {checker2}: {result}")