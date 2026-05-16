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
            if month > 12:
                month -= 12
                year += 1
            elif month < 1:
                month += 12
                year -= 1
        if month == 1:
            if day > 31:
                day = 31
            elif day < 1:
                day = 1
        elif month == 2:
            if day > 28:
                day = 28
            elif day < 1:
                day = 1
        elif month == 3:
            if day > 31:
                day = 31
            elif day < 1:
                day = 1
        elif month == 4:
            if day > 30:
                day = 30
            elif day < 1:
                day = 1
        elif month == 5:
            if day > 31:
                day = 31
            elif day < 1:
                day = 1
        elif month == 6:
            if day > 30:
                day = 30
            elif day < 1:
                day = 1
        elif month == 7:
            if day > 31:
                day = 31
            elif day < 1:
                day = 1
        elif month == 8:
            if day > 31:
                day = 31
            elif day < 1:
                day = 1
        elif month == 9:
            if day > 30:
                day = 30
            elif day < 1:
                day = 1
        elif month == 10:
            if day > 31:
                day = 31
            elif day < 1:
                day = 1
        elif month == 11:
            if day > 30:
                day = 30
            elif day < 1:
                day = 1
        elif month == 12:
            if day > 31:
                day = 31
            elif day < 1:
                day = 1
    return datetime.date(year, month, day)
if __name__ == '__main__':
    date1 = datetime.date(2023, 10, 25)
    shifts1 = [+1, -3, +12]
    result1 = apply_date_shifts(date1, shifts1)
    print(f"Original Date: {date1}")
    print(f"Shifts: {shifts1}")
    print(f"Result 1: {result1}")
    date2 = datetime.date(2024, 1, 31)
    shifts2 = [-1, -1]
    result2 = apply_date_shifts(date2, shifts2)
    print(f"\nOriginal Date: {date2}")
    print(f"Shifts: {shifts2}")
    print(f"Result 2: {result2}")
    date3 = datetime.date(2023, 12, 31)
    shifts3 = [+1, +1]
    result3 = apply_date_shifts(date3, shifts3)
    print(f"\nOriginal Date: {date3}")
    print(f"Shifts: {shifts3}")
    print(f"Result 3: {result3}")
    date4 = datetime.date(2023, 1, 1)
    shifts4 = [-12]
    result4 = apply_date_shifts(date4, shifts4)
    print(f"\nOriginal Date: {date4}")
    print(f"Shifts: {shifts4}")
    print(f"Result 4: {result4}")