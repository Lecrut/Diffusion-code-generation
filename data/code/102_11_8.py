WEEKDAY_LIMIT = 5

def is_weekday(date_str):
    year, month, day = map(int, date_str.split('-'))
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

if __name__ == '__main__':
    sample_date = '2023-10-06'
    print(f"Is {sample_date} a weekday? {is_weekday(sample_date)}")