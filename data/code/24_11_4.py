def is_leap_year(year):
    return (year % 4 == 0) and ((year % 100 != 0) or (year % 400 == 0))

def is_leap_year_bitwise(year):
    return not (year & 3) and ((year & 63) or not (year & 15))

def run_tests():
    test_cases = [
        (2000, True),
        (1900, False),
        (2004, True),
        (2001, False),
        (1600, True),
        (1700, False),
        (1800, False),
        (2000, True),
        (2100, False),
        (2400, True),
        (1, False),
        (4, True),
        (100, False),
        (400, True),
        (2020, True),
        (2021, False),
        (2022, False),
        (2023, False),
        (2024, True)
    ]
    for year, expected in test_cases:
        result_bitwise = is_leap_year_bitwise(year)
        result_regular = is_leap_year(year)
        assert result_bitwise == expected, f"Bitwise failed for {year}: expected {expected}, got {result_bitwise}"
        assert result_regular == expected, f"Regular failed for {year}: expected {expected}, got {result_regular}"
        assert result_bitwise == result_regular, f"Mismatch for {year}: bitwise={result_bitwise}, regular={result_regular}"

if __name__ == '__main__':
    run_tests()
    sample_years = [2000, 1900, 2004, 2001, 1600, 1700, 2020, 2021]
    for year in sample_years:
        print(f"{year}: {is_leap_year_bitwise(year)}")