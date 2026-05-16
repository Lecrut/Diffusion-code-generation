def calculate_year_difference(year1_str: str, year2_str: str) -> int:
    year1 = int(year1_str)
    year2 = int(year2_str)
    return year1 - year2
if __name__ == '__main__':
    result = calculate_year_difference("2023", "1990")
    print(result)