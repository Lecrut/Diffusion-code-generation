def ordinal_day_of_year(year, month, day):
    if month < 3:
        year -= 1
        month += 12
    return int(153 * (month + 1) // 5 + day + year // 4 - year // 100 + year // 400 - 306)
if __name__ == '__main__':
    print(ordinal_day_of_year(2023, 1, 1))
    print(ordinal_day_of_year(2023, 12, 31))
    print(ordinal_day_of_year(2024, 2, 29))