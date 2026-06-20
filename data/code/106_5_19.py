from datetime import date

def calculate_year_difference(date1: date, date2: date) -> int:
    return abs((date2 - date1).days // 365)

if __name__ == '__main__':
    sample_date1 = date(1970, 1, 1)
    sample_date2 = date(2023, 4, 15)
    difference = calculate_year_difference(sample_date1, sample_date2)
    print(difference)