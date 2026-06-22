class NumberChecker:
    def __init__(self, value):
        self.value = value

    def is_greater_than(self, other):
        return self.value > other.value

if __name__ == '__main__':
    VALUE1 = 20
    VALUE2 = 15
    checker1 = NumberChecker(VALUE1)
    checker2 = NumberChecker(VALUE2)
    result = checker1.is_greater_than(checker2)
    print(f"Value {checker1.value} is greater than value {checker2.value}: {result}")