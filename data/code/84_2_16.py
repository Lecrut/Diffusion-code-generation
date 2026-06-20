def day_of_year(year, month, day):
    return (month - 1) * 30 + day + ((month <= 2) + (year % 4 == 0 and year % 100 != 0 or year % 400 == 0)) * (month > 2)

if __name__ == '__main__':
    print(day_of_year(2023, 4, 15))