def compute_year_difference(date1_str: str, date2_str: str) -> int:
    year1 = int(date1_str[0:4])
    year2 = int(date2_str[0:4])
    return abs(year1 - year2)

if __name__ == '__main__':
    sample_date_a = "1995-11-20"
    sample_date_b = "2025-03-15"
    diff = compute_year_difference(sample_date_a, sample_date_b)
    print(diff)