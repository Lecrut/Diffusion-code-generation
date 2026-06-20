def year_difference(year1, year2):
    difference = year1 - year2
    return abs(difference)

if __name__ == '__main__':
    test_cases = [
        (2030, 2015, 15),
        (2000, 2020, -20),
        (1980, 1980, 0),
        (1700, 1800, 100)
    ]
    for year1, year2, expected in test_cases:
        result = year_difference(year1, year2)
        assert result == abs(expected), f"Input: ({year1}, {year2}), Expected: {expected}, Got: {result}"
        print(f"Test passed for ({year1}, {year2}): Result = {result}")
    print("All test cases passed!")