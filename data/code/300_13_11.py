import calendar

def days_remaining(year):
    if not (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return 28
    else:
        return 29

if __name__ == '__main__':
    year = 2023
    print(days_remaining(year))