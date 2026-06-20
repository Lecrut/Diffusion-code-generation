from datetime import date

def calculate_year_difference(date1, date2):
    return abs((date2 - date1).days) // 365

if __name__ == '__main__':
    date1 = date(2010, 1, 1)
    date2 = date(2023, 4, 15)
    print(calculate_year_difference(date1, date2))