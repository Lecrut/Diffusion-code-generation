def ordinal_day_of_year(year, month, day):
    if month < 3:
        year -= 1
        month += 12
    return int((153 * (month + 1) // 5) + day + ((year + year // 4 - year // 100 + year // 400) % 7)) % 365 + 1

if __name__ == '__main__':
    print(ordinal_day_of_year(2023, 4, 15))