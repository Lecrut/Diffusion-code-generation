class ZellerDateCalculator:
    MONTH_ADJUSTMENT = 12
    ZELLER_COEFFICIENT = 13
    DIVISOR = 5
    CENTURY_DIVISOR = 100
    DAY_MAP = {0: "Saturday", 1: "Sunday", 2: "Monday", 3: "Tuesday", 4: "Wednesday", 5: "Thursday", 6: "Friday"}

    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day
        self.adjusted_month = month
        self.adjusted_year = year
        self._adjust_month_and_year()

    def _adjust_month_and_year(self):
        if self.adjusted_month < 3:
            self.adjusted_month += ZellerDateCalculator.MONTH_ADJUSTMENT
            self.adjusted_year -= 1

    def _compute_century_and_year_of_century(self):
        k = self.adjusted_year % ZellerDateCalculator.CENTURY_DIVISOR
        j = self.adjusted_year // ZellerDateCalculator.CENTURY_DIVISOR
        return k, j

    def calculate_day_index(self):
        k, j = self._compute_century_and_year_of_century()
        q = self.day
        m = self.adjusted_month
        h = (q + (ZellerDateCalculator.ZELLER_COEFFICIENT * (m + 1)) // ZellerDateCalculator.DIVISOR + k + k // 4 + j // 4 - 2 * j) % 7
        return h

    def get_day_name(self):
        h = self.calculate_day_index()
        return ZellerDateCalculator.DAY_MAP.get(h, "Unknown")

if __name__ == '__main__':
    calculator = ZellerDateCalculator(1900, 1, 1)
    result = calculator.get_day_name()
    print(result)