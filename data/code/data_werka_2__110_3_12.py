from datetime import date

def sort_dates():
    return sorted([date(2023, 1, 1), date(2022, 12, 31), date(2023, 6, 15), date(2021, 5, 10)])

if __name__ == '__main__':
    print(sort_dates())