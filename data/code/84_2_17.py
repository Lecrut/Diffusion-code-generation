def day_of_year(year, month, day):
    return (year - 1900) * 365 + sum((year // i % 2 == 1 for i in range(1, year))) + sum([31, 28 + (year % 4 == 0 and year % 100 != 0 or year % 400 == 0), 31, 30, 31, 30, 31, 31, 30, 31, 30, 31][:month]) + day

if __name__ == '__main__':
    print(day_of_year(2023, 4, 15))