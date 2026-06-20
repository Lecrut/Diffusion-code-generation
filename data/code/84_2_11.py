import math

def day_of_year(year, month, day):
    return int((30.59 * (month - 1) + day - 1) + (year - 1) * 365 + math.floor((year - 1) / 4) - math.floor((year - 1) / 100) + math.floor((year - 1) / 400))

if __name__ == '__main__':
    print(day_of_year(2023, 4, 15))