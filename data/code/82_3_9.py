def year_differences(years):
    if not all(isinstance(y, int) and y >= 1582 for y in years):
        raise ValueError("All years must be integers greater than or equal to 1582.")
    
    prev_year = None
    for year in years:
        if prev_year is not None:
            yield year - prev_year
        prev_year = year

if __name__ == '__main__':
    sample_years = [1600, 1700, 1800, 1900]
    for diff in year_differences(sample_years):
        print(diff)