class Month:
    def __init__(self, year):
        self.year = year

    def days_in_month(self, month):
        if month == 2:
            return 29 if (self.year % 4 == 0 and self.year % 100 != 0) or self.year % 400 == 0 else 28
        elif month in [4, 6, 9, 11]:
            return 30
        else:
            return 31

if __name__ == '__main__':
    year = 2023
    month_instance = Month(year)
    print(f"Days in February 2023: {month_instance.days_in_month(2)}")
    print(f"Days in April 2023: {month_instance.days_in_month(4)}")