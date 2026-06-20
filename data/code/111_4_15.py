from datetime import date

def total_seconds_in_year(year):
    start_date = date(year, 1, 1)
    end_date = date(year + 1, 1, 1)
    delta = end_date - start_date
    return delta.total_seconds()

if __name__ == '__main__':
    sample_year = 2023
    print(total_seconds_in_year(sample_year))