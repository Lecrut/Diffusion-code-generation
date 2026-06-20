import datetime

def total_seconds_in_non_leap_year():
    months_days = {1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30, 7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}
    total_seconds = sum(months_days.values()) * 24 * 60 * 60
    return total_seconds
if __name__ == '__main__':
    result = total_seconds_in_non_leap_year()
    print(result)