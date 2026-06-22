from datetime import date

def sort_dates():
    return sorted([date(2023, 1, 15), date(2021, 5, 20), date(2022, 12, 1), date(2024, 3, 10)])

if __name__ == '__main__':
    print(sort_dates())