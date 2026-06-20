from datetime import date

def year_difference(date1, date2):
    return abs(date1.year - date2.year)

if __name__ == '__main__':
    sample_date1 = date(2010, 5, 15)
    sample_date2 = date(2023, 8, 20)
    print(year_difference(sample_date1, sample_date2))