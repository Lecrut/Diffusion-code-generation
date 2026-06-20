from datetime import date

def calculate_year_difference(date1, date2):
    return abs((date2 - date1).days // 365)

if __name__ == '__main__':
    sample_date1 = date(1980, 7, 4)
    sample_date2 = date(2023, 10, 11)
    print(calculate_year_difference(sample_date1, sample_date2))