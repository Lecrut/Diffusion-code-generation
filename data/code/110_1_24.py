from datetime import datetime

def sort_datetimes(dates):
    return sorted(dates)

if __name__ == '__main__':
    d1 = datetime(2023, 1, 15, 10, 30)
    d2 = datetime(2022, 12, 31, 23, 59)
    d3 = datetime(2023, 1, 15, 10, 30)
    d4 = datetime(2024, 6, 1, 0, 0)
    original = [d1, d2, d4, d3]
    result = sort_datetimes(original)
    print(result)