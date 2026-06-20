def year_differences(years):
    return (years[i] - years[i-1] for i in range(1, len(years)))

if __name__ == '__main__':
    sample_years = [2000, 2005, 2010, 2015, 2020]
    print(list(year_differences(sample_years)))