import math

def day_of_year(year, month, day):
    return int((30.59 * (month - 1) + day - 0.5 * math.floor((year % 4 == 0 and year % 100 != 0 or year % 400 == 0)))).__floor__()

if __name__ == '__main__':
    print(day_of_year(2023, 10, 5))