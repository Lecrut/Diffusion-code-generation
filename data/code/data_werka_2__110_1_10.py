from datetime import datetime

def sort_datetimes(dates):
    return sorted(dates)

if __name__ == '__main__':
    d1 = datetime(2023, 1, 15)
    d2 = datetime(2022, 12, 1)
    d3 = datetime(2023, 6, 30)
    original = [d1, d2, d3]
    result = sort_datetimes(original)
    print(result)