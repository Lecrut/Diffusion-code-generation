from datetime import date
def days_elapsed(date1: date, date2: date) -> int:
    if date1 < date2:
        return (date2 - date1).days
    else:
        return (date1 - date2).days
if __name__ == '__main__':
    d1 = date(2023, 1, 1)
    d2 = date(2023, 1, 10)
    result1 = days_elapsed(d1, d2)
    print(f"Days elapsed between {d1} and {d2}: {result1}")
    d3 = date(2024, 5, 15)
    d4 = date(2024, 4, 1)
    result2 = days_elapsed(d3, d4)
    print(f"Days elapsed between {d3} and {d4}: {result2}")