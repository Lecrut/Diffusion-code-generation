class NumberChecker:
    def check_odd(self, number):
        return number % 2 != 0

if __name__ == '__main__':
    checker_instance = NumberChecker()
    test_number = 9
    is_odd = checker_instance.check_odd(test_number)
    print(is_odd)