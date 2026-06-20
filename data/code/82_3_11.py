def calculate_year_differences(years):
    if not years or len(years) < 2:
        raise ValueError("At least two years are required")
    
    prev_year = None
    for year in years:
        if prev_year is not None:
            yield year - prev_year
        prev_year = year

if __name__ == '__main__':
    sample_years = [1990, 2000, 2010, 2020]
    for diff in calculate_year_differences(sample_years):
        print(diff)