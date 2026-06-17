def is_leap_year(year):
    if not isinstance(year, int) or year < 0:
        raise ValueError("Year must be a non-negative integer.")
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)
if __name__ == '__main__':
    sample_years = [2000, 1900, 2024, -5]
    for y in sample_years:
        try:
            result = is_leap_year(y)
            print(f"{y} is {'a' if result else 'not a'} leap year.")
        except ValueError as e:
            print(f"Error processing {y}: {e}")