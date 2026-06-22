from datetime import date

def calculate_year_difference(date1: date, date2: date) -> int:
    return abs(date1.year - date2.year)

if __name__ == '__main__':
    d1 = date(2023, 10, 15)
    d2 = date(2015, 5, 20)
    result = calculate_year_difference(d1, d2)
    print(result)