class LeapYearCalculator:
    def __init__(self, year):
        self.year = year

    def is_leap(self):
        if self.year % 400 == 0:
            return True
        if self.year % 100 == 0:
            return False
        if self.year % 4 == 0:
            return True
        return False

if __name__ == '__main__':
    calc1 = LeapYearCalculator(2000)
    print(calc1.is_leap())
    calc2 = LeapYearCalculator(1900)
    print(calc2.is_leap())
    calc3 = LeapYearCalculator(2024)
    print(calc3.is_leap())