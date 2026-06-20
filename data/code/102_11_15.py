def is_weekday(date_str):
    year, month, day = map(int, date_str.split('-'))
    return (year * 365 + month * 30 + day) % 7 < 5

if __name__ == '__main__':
    sample_date1 = '2023-10-23'
    sample_date2 = '2023-10-24'
    print(f"Is {sample_date1} a weekday? {is_weekday(sample_date1)}")
    print(f"Is {sample_date2} a weekday? {is_weekday(sample_date2)}")