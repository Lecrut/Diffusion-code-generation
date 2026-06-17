import calendar
def get_day_of_month(year, month):
    try:
        day = calendar.monthrange(year, month)[0]
        return day
    except ValueError:
        return "Invalid date"
if __name__ == '__main__':
    year1 = 2023
    month1 = 10
    print(f"Day of the month for {year1}-{month1}: {get_day_of_month(year1, month1)}")
    year2 = 2024
    month2 = 2
    print(f"Day of the month for {year2}-{month2}: {get_day_of_month(year2, month2)}")
    year3 = 2023
    month3 = 13
    print(f"Day of the month for {year3}-{month3}: {get_day_of_month(year3, month3)}")