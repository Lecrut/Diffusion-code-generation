def year_difference_generator(years):
    n = len(years)
    for i in range(n - 1):
        yield years[i+1] - years[i]
if __name__ == '__main__':
    sample_years = [2000, 2005, 2010, 2015]
    differences = year_difference_generator(sample_years)
    print(list(differences))