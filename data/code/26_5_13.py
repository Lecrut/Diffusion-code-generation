class NumberChecker:
    def __init__(self, value):
        self.value = value
    
    def is_greater_than(self, other):
        return self.value > other.value

if __name__ == '__main__':
    checker1 = NumberChecker(10)
    checker2 = NumberChecker(5)
    
    result_checker1_vs_2 = checker1.is_greater_than(checker2)
    print(f"{checker1} is greater than {checker2}: {result_checker1_vs_2}")

    checker3 = NumberChecker(8)
    result_checker1_vs_3 = checker1.is_greater_than(checker3)
    print(f"{checker1} is greater than {checker3}: {result_checker1_vs_3}")