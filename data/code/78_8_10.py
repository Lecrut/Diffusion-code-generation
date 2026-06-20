def find_month_difference(month1: int, month2: int) -> int:
    return abs(month1 - month2)

if __name__ == '__main__':
    sample_months = [(5, 10), (12, 3), (7, 7)]
    for month_pair in sample_months:
        print(f"Difference between {month_pair[0]} and {month_pair[1]}: {find_month_difference(*month_pair)}")