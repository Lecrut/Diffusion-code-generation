def is_weekday(year, month, day):
    weekday_map = {
        0: False,
        1: True,
        2: True,
        3: True,
        4: True,
        5: False,
        6: False
    }
    return weekday_map[(year * 365 + month * 30 + day) % 7]

if __name__ == '__main__':
    year1, month1, day1 = 2023, 10, 23
    year2, month2, day2 = 2023, 10, 24
    year3, month3, day3 = 2023, 10, 27
    year4, month4, day4 = 2023, 10, 28

    print(f"Is {year1}-{month1:02d}-{day1:02d} a weekday? {is_weekday(year1, month1, day1)}")
    print(f"Is {year2}-{month2:02d}-{day2:02d} a weekday? {is_weekday(year2, month2, day2)}")
    print(f"Is {year3}-{month3:02d}-{day3:02d} a weekday? {is_weekday(year3, month3, day3)}")
    print(f"Is {year4}-{month4:02d}-{day4:02d} a weekday? {is_weekday(year4, month4, day4)}")