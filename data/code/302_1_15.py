class DateUtils:
    def days_in_month(self, year, month):
        if month == 2:
            return 29 if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0 else 28
        elif month in [4, 6, 9, 11]:
            return 30
        else:
            return 31

if __name__ == '__main__':
    date_utils = DateUtils()
    print(f"Days in February 2020: {date_utils.days_in_month(2020, 2)}")
    print(f"Days in March 2021: {date_utils.days_in_month(2021, 3)}")
    print(f"Days in November 2022: {date_utils.days_in_month(2022, 11)}")