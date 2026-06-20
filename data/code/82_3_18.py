def year_differences(years):
    prev_year = None
    for year in years:
        if prev_year is not None:
            yield year - prev_year
        prev_year = year

if __name__ == '__main__':
    sample_years = [2001, 2006, 2011, 2016]
    for diff in year_differences(sample_years):
        print(diff)