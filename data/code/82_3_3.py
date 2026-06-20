def year_differences(years):
    for i in range(len(years) - 1):
        yield years[i + 1] - years[i]

if __name__ == '__main__':
    sample_years = [2000, 2005, 2010, 2015, 2020]
    for diff in year_differences(sample_years):
        print(diff)