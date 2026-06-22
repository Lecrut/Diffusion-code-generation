class ZellerDate:
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day
        self._adjusted_year = year
        self._adjusted_month = month
        if self._adjusted_month < 3:
            self._adjusted_month += 12
            self._adjusted_year -= 1
        self.k = self._adjusted_year % 100
        self.j = self._adjusted_year // 100

    def calculate_h(self):
        q = self.day
        m = self._adjusted_month
        return (q + (13 * (m + 1)) // 5 + self.k + self.k // 4 + self.j // 4 - 2 * self.j) % 7

    def get_day_name(self):
        h = self.calculate_h()
        names = ["Saturday", "Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
        return names[h]

    def get_day_number(self):
        return self.calculate_h()

if __name__ == '__main__':
    date_obj = ZellerDate(1900, 1, 1)
    print(date_obj.get_day_number())
    print(date_obj.get_day_name())