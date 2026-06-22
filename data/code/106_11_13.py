def compute_year_difference(date1_str: str, date2_str: str) -> int:
    year1 = int(date1_str[:4])
    year2 = int(date2_str[:4])
    return abs(year1 - year2)

if __name__ == '__main__':
    result = compute_year_difference("2020-01-01", "2023-12-31")
    print(result)