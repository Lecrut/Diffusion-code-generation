class ZellerCalculator:
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day
        self.adjusted_month = month
        self.adjusted_year = year
        if self.adjusted_month < 3:
            self.adjusted_month += 12
            self.adjusted_year -= 1
        self.k = self.adjusted_year % 100
        self.j = self.adjusted_year // 100

    def calculate_h(self):
        q = self.day
        m = self.adjusted_month
        h = (q + (13 * (m + 1)) // 5 + self.k + self.k // 4 + self.j // 4 - 2 * self.j) % 7
        return h

    def get_day_name(self):
        h = self.calculate_h()
        names = {0: "Saturday", 1: "Sunday", 2: "Monday", 3: "Tuesday", 4: "Wednesday", 5: "Thursday", 6: "Friday"}
        return names[h]

if __name__ == '__main__':
    calc = ZellerCalculator(1900, 1, 1)
    print(calc.calculate_h())
    print(calc.get_day_name())