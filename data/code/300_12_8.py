class Month:
    def __init__(self, year, month):
        self.year = year
        self.month = month

    def days_in_month(self):
        if self.month == 2:
            is_leap = self.year % 4 == 0 and (self.year % 100 != 0 or self.year % 400 == 0)
            return 29 if is_leap else 28
        elif self.month in [4, 6, 9, 11]:
            return 30
        else:
            return 31

if __name__ == '__main__':
    month_2023_feb = Month(2023, 2)
    print(month_2023_feb.days_in_month())
    
    month_2024_feb = Month(2024, 2)
    print(month_2024_feb.days_in_month())
    
    month_2023_apr = Month(2023, 4)
    print(month_2023_apr.days_in_month())