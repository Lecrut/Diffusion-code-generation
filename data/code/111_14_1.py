import datetime
def apply_date_shifts(date_obj, shifts):
    year = date_obj.year
    month = date_obj.month
    day = date_obj.day
    for shift in shifts:
        if shift == 0:
            continue
        if shift == 1:
            month += 1
            if month > 12:
                month = 1
                year += 1
        elif shift == -1:
            month -= 1
            if month < 1:
                month = 12
                year -= 1
        elif shift > 1 or shift < -1:
            year += shift // 12
            month += shift % 12
            total_months_shift = shift
            new_year = year + (total_months_shift // 12)
            new_month = month + (total_months_shift % 12)
            if new_month > 12:
                new_year += 1
                new_month -= 12
            elif new_month < 1:
                new_year -= 1
                new_month += 12
            year = new_year
            month = new_month
            try:
                day = day
            except ValueError:
                _, last_day = datetime.date(year, month, 1)
                day = last_day
        else:
            pass
    current_year = date_obj.year
    current_month = date_obj.month
    current_day = date_obj.day
    for shift in shifts:
        if shift == 0:
            continue
        total_months_to_add = shift
        new_total_months = (current_year * 12 + current_month) + total_months_to_add
        new_year = (new_total_months // 12)
        new_month = (new_total_months % 12) + 1
        if new_month == 0:
            new_month = 12
            new_year -= 1
        current_year = new_year
        current_month = new_month
        try:
            datetime.date(current_year, current_month, current_day)
        except ValueError:
            _, last_day = datetime.date(current_year, current_month + 1, 1)
            current_day = last_day - 1
    return datetime.date(current_year, current_month, current_day)
if __name__ == '__main__':
    date1 = datetime.date(2023, 10, 15)
    shifts1 = [+1, -3, +12]
    result1 = apply_date_shifts(date1, shifts1)
    print(f"Original Date: {date1}")
    print(f"Shifts: {shifts1}")
    print(f"Result: {result1}")
    date2 = datetime.date(2024, 1, 31)
    shifts2 = [-1, -1]
    result2 = apply_date_shifts(date2, shifts2)
    print(f"\nOriginal Date: {date2}")
    print(f"Shifts: {shifts2}")
    print(f"Result: {result2}")
    date3 = datetime.date(2023, 1, 1)
    shifts3 = [+12]
    result3 = apply_date_shifts(date3, shifts3)
    print(f"\nOriginal Date: {date3}")
    print(f"Shifts: {shifts3}")
    print(f"Result: {result3}")
    date4 = datetime.date(2023, 2, 28)
    shifts4 = [+1]
    result4 = apply_date_shifts(date4, shifts4)
    print(f"\nOriginal Date: {date4}")
    print(f"Shifts: {shifts4}")
    print(f"Result: {result4}")
    date5 = datetime.date(2023, 1, 31)
    shifts5 = [-1]
    result5 = apply_date_shifts(date5, shifts5)
    print(f"\nOriginal Date: {date5}")
    print(f"Shifts: {shifts5}")
    print(f"Result: {result5}")