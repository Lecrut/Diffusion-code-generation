class NumberChecker:

    def check_odd(self, number):
        return number % 2 != 0
if __name__ == '__main__':
    number_checker = NumberChecker()
    test_number = 15
    is_odd = number_checker.check_odd(test_number)
    print(is_odd)
    another_test_number = 22
    is_another_odd = number_checker.check_odd(another_test_number)
    print(is_another_odd)