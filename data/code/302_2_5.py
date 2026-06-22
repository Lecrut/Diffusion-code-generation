def day_number_in_month(year, month):
    if month == 2:
        return 29 if year % 4 == 0 and year % 100 != 0 or year % 400 == 0 else 28
    elif month in [4, 6, 9, 11]:
        return 30
    else:
        return 31
if __name__ == '__main__':
    print(day_number_in_month(2020, 2))
    print(day_number_in_month(2021, 2))
    print(day_number_in_month(2023, 4))