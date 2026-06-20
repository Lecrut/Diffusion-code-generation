from datetime import date

def are_same_day(date1: date, date2: date) -> bool:
    return date1.year == date2.year and date1.month == date2.month and date1.day == date2.day

if __name__ == '__main__':
    d1 = date(2023, 10, 26)
    d2 = date(2023, 10, 26)
    d3 = date(2023, 11, 1)
    d4 = date(2023, 10, 25)
    print(f"Are {d1} and {d2} on the same day? {are_same_day(d1, d2)}")
    print(f"Are {d1} and {d3} on the same day? {are_same_day(d1, d3)}")
    print(f"Are {d3} and {d1} on the same day? {are_same_day(d3, d1)}")
    print(f"Are {d4} and {d1} on the same day? {are_same_day(d4, d1)}")
    print(f"Are {d2} and {d4} on the same day? {are_same_day(d2, d4)}")