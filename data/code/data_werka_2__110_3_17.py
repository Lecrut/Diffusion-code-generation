from datetime import date

def sort_hardcoded_dates():
    raw_dates = [date(2023, 1, 15), date(2020, 5, 1), date(2021, 12, 25)]
    return sorted([d for d in raw_dates])

if __name__ == '__main__':
    print(sort_hardcoded_dates())