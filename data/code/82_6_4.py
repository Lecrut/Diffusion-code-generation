def year_difference(year1, year2):
    return year1 - year2

if __name__ == '__main__':
    test_cases = {
        (2024, 2020): 4,
        (1990, 2000): -10,
        (2025, 2025): 0,
        (1800, 1750): 50
    }
    
    for year_pair, expected in test_cases.items():
        result = year_difference(*year_pair)
        assert result == expected, f"Input: {year_pair}, Expected: {expected}, Got: {result}"
        print(f"Test passed for {year_pair}: Result = {result}")