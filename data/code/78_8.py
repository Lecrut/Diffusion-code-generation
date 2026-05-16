def calculate_month_difference(date1: tuple[int, int], date2: tuple[int, int]) -> int:
    year1, month1 = date1
    year2, month2 = date2
    diff = (year2 - year1) * 12 + (month2 - month1)
    return abs(diff)
if __name__ == '__main__':
    date_a = (2023, 10)
    date_b = (2024, 3)
    date_c = (2020, 1)
    date_d = (2020, 12)
    date_e = (2025, 1)
    date_f = (2025, 1)
    date_g = (2023, 10)
    print(f"Difference between {date_a} and {date_b}: {calculate_month_difference(date_a, date_b)}")
    print(f"Difference between {date_c} and {date_d}: {calculate_month_difference(date_c, date_d)}")
    print(f"Difference between {date_e} and {date_f}: {calculate_month_difference(date_e, date_f)}")
    print(f"Difference between {date_g} and {date_a}: {calculate_month_difference(date_g, date_a)}")