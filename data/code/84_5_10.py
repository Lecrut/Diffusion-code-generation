def get_day_number(year: int, month: int, day: int) -> int:
    months = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
        months[2] = 29
    return sum(months[:month]) + day
if __name__ == '__main__':
    print(get_day_number(2020, 3, 1))
    print(get_day_number(2019, 3, 1))