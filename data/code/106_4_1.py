def year_difference(years):
    if not years:
        return 0
    return max(years) - min(years)
if __name__ == '__main__':
    sample_years = [2020, 1995, 2023, 1980, 2024]
    result = year_difference(sample_years)
    print(result)