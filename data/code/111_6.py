from datetime import date
import calendar
def shift_date_by_months(start_date, months_to_add):
    if months_to_add == 0:
        return start_date
    year = start_date.year
    month = start_date.month
    total_months = month + months_to_add
    new_year = year + (total_months - 1) // 12
    new_month = (total_months - 1) % 12 + 1
    try:
        new_date = date(new_year, new_month, start_date.day)
        return new_date
    except ValueError:
        return date(new_year, new_month, 1)                                                          
if __name__ == '__main__':
    date1 = date(2023, 3, 15)
    months1 = 3
    result1 = shift_date_by_months(date1, months1)
    print(f"Start Date: {date1}, Add Months: {months1}, Result: {result1}")
    date2 = date(2023, 10, 20)
    months2 = 5
    result2 = shift_date_by_months(date2, months2)
    print(f"Start Date: {date2}, Add Months: {months2}, Result: {result2}")
    date3 = date(2024, 1, 31)
    months3 = 1
    result3 = shift_date_by_months(date3, months3)
    print(f"Start Date: {date3}, Add Months: {months3}, Result: {result3}")
    date4 = date(2024, 12, 10)
    months4 = 2
    result4 = shift_date_by_months(date4, months4)
    print(f"Start Date: {date4}, Add Months: {months4}, Result: {result4}")
    date5 = date(2023, 11, 1)
    months5 = 12
    result5 = shift_date_by_months(date5, months5)
    print(f"Start Date: {date5}, Add Months: {months5}, Result: {result5}")