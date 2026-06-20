from datetime import date

def day_of_year(year, month, day):
    return (date(year, month, day) - date(year, 1, 1)).days + 1

if __name__ == '__main__':
    print(day_of_year(2023, 4, 15))