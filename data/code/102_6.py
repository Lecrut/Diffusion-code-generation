from datetime import date
if __name__ == '__main__':
    d1 = date(2023, 10, 23)
    d2 = date(2023, 10, 24)
    d3 = date(2023, 10, 25)
    d4 = date(2023, 10, 26)
    print(f"Day {d1}: {d1.weekday()}")
    print(f"Day {d2}: {d2.weekday()}")
    print(f"Day {d3}: {d3.weekday()}")
    print(f"Day {d4}: {d4.weekday()}")
    if d1.weekday() == 0:
        print(f"Day {d1} is a Monday (0)")
    if d2.weekday() == 5:
        print(f"Day {d2} is a Saturday (5)")
    if d3.weekday() == 6:
        print(f"Day {d3} is a Sunday (6)")
    if d4.weekday() == 1:
        print(f"Day {d4} is a Tuesday (1)")