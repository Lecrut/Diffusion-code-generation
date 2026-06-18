def calculate_leap_year_status(year: int) -> bool:
    if year % 400 == 0:
        return True
    elif year % 100 == 0:
        return False
    else:
        if year % 4 == 0:
            return True
        else:
            return False
if __name__ == '__main__':
    test_years = [2024, 1900, 2000, 2023, 1600]
    print("Leap Year Status Calculation Results:")
    for year in test_years:
        is_leap = calculate_leap_year_status(year)
        status_str = "LEAP YEAR" if is_leap else "NOT A LEAP YEAR"
        print(f"{year}: {status_str}")
    assert calculate_leap_year_status(2024) == True, "2024 should be a leap year."
    assert calculate_leap_year_status(1900) == False, "1900 is divisible by 100 but not 400."
    assert calculate_leap_year_status(2000) == True, "2000 is divisible by 400."
    print("\nAll assertions passed successfully.")