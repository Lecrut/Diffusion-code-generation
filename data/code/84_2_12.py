def day_of_year(year, month, day):
    return (year - 1900) * 365 + sum([31 if m in {1, 3, 5, 7, 8, 10, 12} else 30 for m in range(1, month)]) + day + ((year % 4 == 0 and year % 100 != 0) or (year % 400 == 0))

if __name__ == '__main__':
    print(day_of_year(2023, 4, 15))