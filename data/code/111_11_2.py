import datetime
def manipulate_date_components(date_obj, shift):
    year = date_obj.year
    month = date_obj.month
    new_month = month + shift
    year_change = year // 12
    new_year = year + year_change
    new_month = new_month % 12
    if new_month <= 0:
        new_month += 12
    if new_month == 12:
        new_year += 1
        new_month = 1
    if new_month > 12:
        new_year += 1
        new_month = new_month - 12
    return datetime.date(new_year, new_month, date_obj.day)
if __name__ == '__main__':
    date1 = datetime.date(2023, 10, 15)
    shift1 = 3
    result1 = manipulate_date_components(date1, shift1)
    print(f"Original Date: {date1}, Shift: {shift1}, Result: {result1}")
    date2 = datetime.date(2023, 1, 10)
    shift2 = -5
    result2 = manipulate_date_components(date2, shift2)
    print(f"Original Date: {date2}, Shift: {shift2}, Result: {result2}")
    date3 = datetime.date(2023, 12, 25)
    shift3 = 1
    result3 = manipulate_date_components(date3, shift3)
    print(f"Original Date: {date3}, Shift: {shift3}, Result: {result3}")
    date4 = datetime.date(2023, 1, 1)
    shift4 = 13
    result4 = manipulate_date_components(date4, shift4)
    print(f"Original Date: {date4}, Shift: {shift4}, Result: {result4}")
    date5 = datetime.date(2023, 5, 1)
    shift5 = -12
    result5 = manipulate_date_components(date5, shift5)
    print(f"Original Date: {date5}, Shift: {shift5}, Result: {result5}")