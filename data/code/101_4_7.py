import datetime
def day_of_week_first_of_month(year, month):
    date = datetime.date(year, month, 1)
    return date.weekday()
if __name__ == '__main__':
    year1 = 2023
    month1 = 1
    result1 = day_of_week_first_of_month(year1, month1)
    print(f"Year: {year1}, Month: {month1}, Day of the week for the 1st: {result1}")
    year2 = 2024
    month2 = 12
    result2 = day_of_week_first_of_month(year2, month2)
    print(f"Year: {year2}, Month: {month2}, Day of the week for the 1st: {result2}")
    year3 = 2025
    month3 = 3
    result3 = day_of_week_first_of_month(year3, month3)
    print(f"Year: {year3}, Month: {month3}, Day of the week for the 1st: {result3}")