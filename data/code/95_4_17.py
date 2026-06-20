class NumberChecker:
    def __init__(self, numbers):
        self.numbers = numbers

    def check_conditions(self):
        count = 0
        for num in self.numbers:
            if num > 0 and num % 2 == 0:
                count += 1
        return count >= 3

if __name__ == '__main__':
    checker1 = NumberChecker([2, 4, 6, 1, 3, 5])
    checker2 = NumberChecker([1, 3, 5, 7, 9])
    checker3 = NumberChecker([2, 4, 6, 8, 10])
    checker4 = NumberChecker([2, 4, 1, 3])

    print(f"Sample List 1: {checker1.check_conditions()}")
    print(f"Sample List 2: {checker2.check_conditions()}")
    print(f"Sample List 3: {checker3.check_conditions()}")
    print(f"Sample List 4: {checker4.check_conditions()}")