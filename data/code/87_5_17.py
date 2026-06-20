class EvenGreaterChecker:
    def __init__(self, numbers):
        self.numbers = numbers
    
    def check_flag(self):
        flag = False
        for number in self.numbers:
            if number % 2 == 0 and number > 50:
                flag = True
        return flag

if __name__ == '__main__':
    checker1 = EvenGreaterChecker([45, 60, 75, 80])
    print(f"Flag for [45, 60, 75, 80]: {checker1.check_flag()}")
    
    checker2 = EvenGreaterChecker([30, 40, 50, 60])
    print(f"Flag for [30, 40, 50, 60]: {checker2.check_flag()}")