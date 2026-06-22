def days_in_month(year, month):
    if not (1 <= month <= 12):
        raise ValueError("Month must be between 1 and 12")
    
    days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if month == 2:
        is_leap = (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)
        return days[month] + is_leap
    else:
        return days[month]

if __name__ == '__main__':
    print(days_in_month(2023, 10))
    print(days_in_month(2024, 2))