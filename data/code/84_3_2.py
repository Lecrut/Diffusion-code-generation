def day_of_year(year, month, day):
    return 365 * (year - 1) + (month - 1) * 30 + day
if __name__ == '__main__':
    print(day_of_year(2023, 10, 27))