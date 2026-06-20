YEAR_BASE = 2000

def year_difference(y1, y2):
    return abs(y1 - y2)

if __name__ == '__main__':
    sample_years_1 = 2023
    sample_years_2 = 1998
    print(year_difference(sample_years_1, sample_years_2))