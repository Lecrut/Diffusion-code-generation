def is_leap_year(year):
    return (year & 3 == 0) and ((year % 100 != 0) or (year % 400 == 0))

def run_tests():
    test_cases = [
        (1, False),
        (2, False),
        (3, False),
        (4, True),
        (100, False),
        (400, True),
        (800, True),
        (2000, True),
        (1900, False),
        (2024, True),
        (2023, False),
        (2400, True),
        (2100, False),
        (0, True),
        (1600, True),
        (1700, False),
        (1800, False),
        (1999, False),
        (2001, False),
        (2028, True),
    ]
    results = []
    for year, expected in test_cases:
        result = is_leap_year(year)
        results.append((year, expected, result, result == expected))
        assert result == expected, f"Failed for year {year}: expected {expected}, got {result}"
    return results

if __name__ == '__main__':
    test_results = run_tests()
    print(test_results)