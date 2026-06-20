class OddChecker:
    def is_odd(self, num):
        return num & 1 != 0

if __name__ == '__main__':
    checker = OddChecker()
    print(f"Is 4 odd? {checker.is_odd(4)}")
    print(f"Is 5 odd? {checker.is_odd(5)}")