def is_weekday(date_str):
    year, month, day = map(int, date_str.split('-'))
    return (year > 0 and month > 0 and month < 13 and day > 0 and 
            day <= [31, 29 if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0 else 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31][month - 1])

if __name__ == '__main__':
    sample_dates = ['2023-10-06', '2023-10-07', '2024-02-29', '2023-02-28']
    for date_str in sample_dates:
        print(f"Is {date_str} a weekday? {is_weekday(date_str)}")