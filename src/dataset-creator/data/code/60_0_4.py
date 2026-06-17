def is_leap_year(year):
    try:
        year = int(year)
        if not isinstance(year, (int, float)):
            raise TypeError("Year must be an integer.")
        return bool((year % 4 == 0 and year % 100 != 0) or (year % 400 == 0))
    except ValueError:
        print(f"Error: Invalid input '{year}'. Please provide a valid integer year.")
        raise
if __name__ == '__main__':
    sample_years = [2000, 1900, 2024, "invalid", None]
    for test_year in sample_years:
        try:
            result = is_leap_year(test_year)
            print(f"{test_year} is {'a' if result else 'not a'} leap year.")
        except Exception as e:
            print(f"Error processing {test_year}: {e}")