class LeapYearChecker:
    def __init__(self):
        self.divisors = [4, 100, 400]

    def is_leap(self, year):
        divisible_by_4 = year % self.divisors[0] == 0
        divisible_by_100 = year % self.divisors[1] == 0
        divisible_by_400 = year % self.divisors[2] == 0

        if divisible_by_400:
            return True
        if divisible_by_100:
            return False
        return divisible_by_4

if __name__ == '__main__':
    checker = LeapYearChecker()
    print(checker.is_leap(2000))
    print(checker.is_leap(1900))
    print(checker.is_leap(2024))
    print(checker.is_leap(2023))
    print(checker.is_leap(2004))