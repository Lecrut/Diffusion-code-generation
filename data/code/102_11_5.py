def is_weekday(date_str):
    day_of_week = int(date_str[8:])
    return 1 <= day_of_week <= 5

if __name__ == '__main__':
    date1 = '2023-10-23'
    date2 = '2023-10-24'
    date3 = '2023-10-27'
    date4 = '2023-10-28'
    print(f"Is {date1} a weekday? {is_weekday(date1)}")
    print(f"Is {date2} a weekday? {is_weekday(date2)}")
    print(f"Is {date3} a weekday? {is_weekday(date3)}")
    print(f"Is {date4} a weekday? {is_weekday(date4)}")