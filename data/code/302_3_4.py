days_per_month = {
    1: 31,
    2: 28,
    3: 31,
    4: 30,
    5: 31,
    6: 30,
    7: 31,
    8: 31,
    9: 30,
    10: 31,
    11: 30,
    12: 31
}

def days_in_month(year):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return {month: days for month, days in days_per_month.items() if month == 2}
    else:
        return days_per_month

if __name__ == '__main__':
    print(days_in_month(2024))
    print(days_in_month(2023))