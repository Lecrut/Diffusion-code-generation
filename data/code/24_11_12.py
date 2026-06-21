def is_leap_bitwise(year):
    return (not (year & 3)) and ((year & 15) or not (year & 63))

def run_tests():
    test_cases = [
        (2000, True),
        (1900, False),
        (2004, True),
        (2001, False),
        (1600, True),
        (1700, False),
        (1800, False),
        (1904, True),
        (2100, False),
        (2400, True),
        (1, False),
        (4, True),
        (0, True),
        (-4, True),
        (100, False),
        (400, True),
        (2023, False),
        (2024, True),
        (10000, True),
        (9999, False)
    ]
    for year, expected in test_cases:
        assert is_leap_bitwise(year) == expected, f"Failed for year {year}: expected {expected}, got {is_leap_bitwise(year)}"
    print("All tests passed")

if __name__ == '__main__':
    run_tests()
    print(is_leap_bitwise(2000))
    print(is_leap_bitwise(1900))
    print(is_leap_bitwise(2004))
    print(is_leap_bitwise(2001))