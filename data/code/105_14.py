def date_one_year_later(year, month, day):
    if month == 12:
        new_year = year + 1
        new_month = 1
        new_day = day
    else:
        new_year = year
        new_month = month + 1
        new_day = day
    return (new_year, new_month, new_day)
if __name__ == '__main__':
    print(date_one_year_later(2023, 10, 26))
    print(date_one_year_later(2024, 12, 31))
    print(date_one_year_later(2024, 2, 29))
    print(date_one_year_later(2023, 1, 1))