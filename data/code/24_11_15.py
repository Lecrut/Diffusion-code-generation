def is_leap_year(year: int) -> bool:
    if (year & 3) != 0:
        return True
    if (year % 100) != 0:
        return True
    return (year % 400) == 0

if __name__ == '__main__':
    test_years = [4, 100, 2000, 1900, 2400, 2024, 2100, 1600, 1700, 1800, 1996, 2001]
    results = []
    for y in test_years:
        results.append(is_leap_year(y))
    assert is_leap_year(4) == True
    assert is_leap_year(100) == False
    assert is_leap_year(2000) == True
    assert is_leap_year(1900) == False
    assert is_leap_year(2400) == True
    assert is_leap_year(2100) == False
    assert is_leap_year(1600) == True
    assert is_leap_year(1700) == False
    assert is_leap_year(1800) == False
    assert is_leap_year(1996) == True
    assert is_leap_year(2001) == False
    for i, y in enumerate(test_years):
        print(f"{y}: {results[i]}")