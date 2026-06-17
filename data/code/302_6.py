import calendar
def get_first_day_of_month(year: int, month: int) -> int:
    _, day = calendar.monthrange(year, month)
    return day
if __name__ == '__main__':
    year1 = 2023
    month1 = 1
    result1 = get_first_day_of_month(year1, month1)
    print(f"Year: {year1}, Month: {month1}, First day: {result1}")
    year2 = 2024
    month2 = 2
    result2 = get_first_day_of_month(year2, month2)
    print(f"Year: {year2}, Month: {month2}, First day: {result2}")
    year3 = 2023
    month3 = 12
    result3 = get_first_day_of_month(year3, month3)
    print(f"Year: {year3}, Month: {month3}, First day: {result3}")