def is_leap_year(year):
    if not isinstance(year, int) or year < 1:
        raise ValueError("Year must be a positive integer.")
    
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    else:
        return False

if __name__ == '__main__':
    sample_years = [2000, 1900, 2020, 2023]
    results = {year: is_leap_year(year) for year in sample_years}
    
    for year, result in results.items():
        print(f"Year: {year}, Leap Year: {result}")