class LeapYearChecker:
    def is_leap(self, year):
        if year % 400 == 0:
            return True
        if year % 100 == 0:
            return False
        return year % 4 == 0

if __name__ == '__main__':
    checker = LeapYearChecker()
    print(checker.is_leap(2000))
    print(checker.is_leap(1900))
    print(checker.is_leap(2024))