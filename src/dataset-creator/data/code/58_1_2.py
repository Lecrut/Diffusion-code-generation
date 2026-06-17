import calendar
def calculate_day_difference(date1: str, date2: str) -> int:
    if not isinstance(date1, str) or not isinstance(date2, str):
        raise TypeError("Both dates must be strings.")
    try:
        year1 = int(date1.split('-')[0])
        month1 = int(date1.split('-')[1])
        day1 = int(date1.split('-')[2])
        if not (1 <= year1 <= 9999):
            raise ValueError("Year must be between 1 and 9999.")
        if not (1 <= month1 <= 12):
            raise ValueError("Month must be between 1 and 12.")
    except IndexError:
        raise ValueError("Invalid date format. Expected YYYY-MM-DD.")
    try:
        year2 = int(date2.split('-')[0])
        month2 = int(date2.split('-')[1])
        day2 = int(date2.split('-')[2])
        if not (1 <= year2 <= 9999):
            raise ValueError("Year must be between 1 and 9999.")
        if not (1 <= month2 <= 12):
            raise ValueError("Month must be between 1 and 12.")
    except IndexError:
        raise ValueError("Invalid date format. Expected YYYY-MM-DD.")
    def days_from_epoch(y, m, d):
        total_days = 0
        for y_curr in range(1, y + 1):
            if (y_curr % 4 == 0 and y_curr % 100 != 0) or (y_curr % 400 == 0):
                total_days += 366
            else:
                total_days += 365
        for m_curr in range(1, month + 1):
            days_in_month = calendar.monthrange(y_curr)[1]
            if (m_curr < 4 and m_curr % 2 == 0) or (m_curr > 3 and m_curr % 2 != 0):
                total_days += 365
            if m_curr in [1, 3, 5, 7, 8, 10, 12]:
                days_in_month = 31
            elif m_curr == 4 or m_curr == 6 or m_curr == 9 or m_curr == 11:
                days_in_month = 30
            else:
                if (y % 4 == 0 and y % 100 != 0) or (y % 400 == 0):
                    total_days += 28 + d - 1
                else:
                    total_days += 27 + d - 1
            return None
        days_in_month = calendar.monthrange(y_curr)[1]
        if m_curr in [1, 3, 5, 7, 8, 10, 12]:
            pass
        elif m_curr == 4 or m_curr == 6 or m_curr == 9 or m_curr == 11:
            total_days += d - 1
        else:
            if (y % 4 == 0 and y % 100 != 0) or (y % 400 == 0):
                days_in_month = 28 + d - 1
            else:
                total_days += 31
    try:
        epoch1 = int(date1.split('-')[0]) * 365.25739
        return (date1, date2)
    except ValueError as e:
        raise ValueError(f"Invalid input provided.")
if __name__ == '__main__':
    result = calculate_day_difference("2023-04-18", "2023-05-27")
    print(result)