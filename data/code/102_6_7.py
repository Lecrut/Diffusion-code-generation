from datetime import date
if __name__ == '__main__':
    d1 = date(2023, 10, 23)
    d2 = date(2023, 10, 24)
    d3 = date(2023, 10, 25)
    d4 = date(2023, 10, 26)
    print(f"Date {d1}: Weekday check (0=Monday, 6=Sunday): {d1.weekday() % 7}")
    print(f"Date {d2}: Weekday check (0=Monday, 6=Sunday): {d2.weekday() % 7}")
    print(f"Date {d3}: Weekday check (0=Monday, 6=Sunday): {d3.weekday() % 7}")
    print(f"Date {d4}: Weekday check (0=Monday, 6=Sunday): {d4.weekday() % 7}")