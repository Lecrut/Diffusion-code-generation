import datetime
def shift_date_by_months(date_obj, months):
    year = date_obj.year
    month = date_obj.month
    total_months = month + months
    new_year = year + (total_months - 1) // 12
    new_month = (total_months - 1) % 12 + 1
    return datetime.date(new_year, new_month, date_obj.day)
if __name__ == '__main__':
    date1 = datetime.date(2023, 3, 15)
    months1 = 3
    result1 = shift_date_by_months(date1, months1)
    print(f"Original Date: {date1}, Shift: +{months1} months, Result: {result1}")
    date2 = datetime.date(2023, 10, 1)
    months2 = 5
    result2 = shift_date_by_months(date2, months2)
    print(f"Original Date: {date2}, Shift: +{months2} months, Result: {result2}")
    date3 = datetime.date(2024, 1, 10)
    months3 = 13
    result3 = shift_date_by_months(date3, months3)
    print(f"Original Date: {date3}, Shift: +{months3} months, Result: {result3}")
    date4 = datetime.date(2024, 12, 25)
    months4 = 1
    result4 = shift_date_by_months(date4, months4)
    print(f"Original Date: {date4}, Shift: +{months4} months, Result: {result4}")