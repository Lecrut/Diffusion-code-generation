def validate_year(year_str: str) -> int:
    year = int(year_str)
    if year < 1400 or year > 2100:
        raise ValueError("Year must be between 1400 and 2100 inclusive.")
    return year

def calculate_year_difference(year1_str: str, year2_str: str) -> int:
    year1 = validate_year(year1_str)
    year2 = validate_year(year2_str)
    return abs(year1 - year2)

if __name__ == '__main__':
    year_a = "2020"
    year_b = "1990"
    difference = calculate_year_difference(year_a, year_b)
    print(difference)

    year_c = "2023"
    year_d = "2010"
    difference = calculate_year_difference(year_c, year_d)
    print(difference)

    year_e = "1500"
    year_f = "1600"
    difference = calculate_year_difference(year_e, year_f)
    print(difference)

    year_g = "2100"
    year_h = "2000"
    difference = calculate_year_difference(year_g, year_h)
    print(difference)