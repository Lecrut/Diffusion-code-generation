def is_leap_year(year):
    try:
        year = int(year)
        if not isinstance(year, (int, float)):
            raise ValueError("Year must be an integer.")
        return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)
    except Exception as e:
        print(f"Error processing input: {e}")
        return False
if __name__ == '__main__':
    sample_years = [2000, 1900, 2023, -5]
    for year in sample_years:
        result = is_leap_year(year)
        print(f"{year} is {'a' if result else 'not a'} leap year.")