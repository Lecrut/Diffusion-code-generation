import calendar

def is_weekday(date_str):
    parts = date_str.split('-')
    year = int(parts[0])
    month = int(parts[1])
    day = int(parts[2])
    return calendar.isleap(year) or calendar.isleap(month) or calendar.isleap(day)

if __name__ == '__main__':
    print(is_weekday('2023-10-01'))
    print(is_weekday('2024-02-29'))