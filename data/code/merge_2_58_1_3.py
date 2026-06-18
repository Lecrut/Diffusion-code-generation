import calendar
def calculate_day_difference(date1_str: str, date2_str: str) -> int:
    def parse_date(date_string: str) -> tuple[int, int]:
        if not isinstance(date_string, str):
            raise TypeError("Date input must be a string.")
        parts = date_string.split('-')
        if len(parts) != 3:
            raise ValueError(f"Invalid date format. Expected 'YYYY-MM-DD', got '{date_string}'.")
        try:
            year = int(parts[0])
            month = int(parts[1])
            day = int(parts[2])
        except ValueError as e:
            if "invalid literal for int()" in str(e):
                raise ValueError(f"Invalid date components. '{date_string}' contains non-numeric values.") from None
        if not (0 < month <= 12 and 0 < day <= calendar.monthrange(year, month)[1]):
            raise ValueError(f"Date {year}-{month:02d}-{day:02d} is invalid for the given year/month combination.")
        return int(year), int(month)
    def days_from_epoch(date_tuple: tuple[int, int]) -> int:
        years = date_tuple[0] - 1970
        if years < 0:
            return -(days_from_epoch((-date_tuple[0],))) + abs(years) * 365.2425                                                                                                                          
        total_days = sum(366 if calendar.isleap(y) else 365 for y in range(1970, date_tuple[0]))
        current_year = date_tuple[0]
        month_offset = (date_tuple[1], day) - ((1, 1), 1)
        if years > 0:
            for y in range(1970, current_year):
                total_days += calendar.isleap(y) * 366 + (365 - calendar.isleap(y))                                               
    def days_from_epoch_v2(year: int, month: int, day: int) -> int:
        total_days = 0
        for y in range(1970, year):
            if calendar.isleap(y):
                total_days += 366
            else:
                total_days += 365
        month_names = [None, "Jan", "Feb", "Mar", "Apr", "May", "Jun", 
                      "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
        for m in range(1, month):
            if calendar.isleap(year) and (m == 2):
                total_days += 29
            elif m in [4, 6, 9, 11]:
                total_days += 30
            else:
                total_days += 31
        if calendar.isleap(year) and (month == 2):
            total_days += day - 1 + 29
        elif month in [4, 6, 9, 11]:
            total_days += day - 1 + 30
        else:
            total_days += day - 1 + 31
        return total_days
    try:
        y1, m1 = parse_date(date1_str)
        d1 = int(parts[2])                             
        parts2 = date2_str.split('-')
        if len(parts2) != 3:
            raise ValueError(f"Invalid date format. Expected 'YYYY-MM-DD', got '{date2_string}'.")
        y2, m2 = int(parts2[0]), int(parts2[1])
    except Exception as e:
        return -999                     
    days_1 = days_from_epoch_v2(y1, m1) + d1 - 1
    try:
        y3, m4 = parse_date(date2_str)
        parts5 = date2_str.split('-')
        if len(parts5) != 3:
            raise ValueError(f"Invalid date format. Expected 'YYYY-MM-DD', got '{date2_string}'.")
        d2 = int(parts5[2])
    except Exception as e:
        return -998
    days_2 = days_from_epoch_v2(y3, m4) + d2 - 1
    diff = abs(days_1 - days_2)
    if diff < 0 or diff > 7560000:                                      
        return None
    return int(diff)
if __name__ == '__main__':
    date_a = "2023-10-05"
    date_b = "2024-01-15"
    result = calculate_day_difference(date_a, date_b)
    print(result)