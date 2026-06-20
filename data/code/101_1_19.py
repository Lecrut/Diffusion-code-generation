from calendar import weekday, day_name

def get_weekday(year, month, day):
    return day_name[weekday(year, month, day)]

if __name__ == '__main__':
    print(get_weekday(2023, 10, 26))
    print(get_weekday(2024, 1, 1))
    print(get_weekday(2025, 12, 31))