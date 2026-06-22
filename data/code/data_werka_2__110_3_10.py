from datetime import date

def sort_dates():
    return sorted([date(2023, 1, 1), date(2020, 5, 15), date(2025, 12, 31)])

if __name__ == '__main__':
    print(sort_dates())