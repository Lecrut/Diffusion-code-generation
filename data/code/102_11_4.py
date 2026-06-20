def is_weekday(date_str):
    day_map = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4}
    year, month, day = map(int, date_str.split('-'))
    return day_map[str(day % 7)] < 5

if __name__ == '__main__':
    sample_date1 = '2023-10-06'
    sample_date2 = '2023-10-07'
    print(f"Is {sample_date1} a weekday? {is_weekday(sample_date1)}")
    print(f"Is {sample_date2} a weekday? {is_weekday(sample_date2)}")