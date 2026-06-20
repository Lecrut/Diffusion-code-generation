from datetime import date

def get_day_of_specific_date(year=2024, month=10, day=10):
    return date(year, month, day).day

if __name__ == '__main__':
    specific_sample_date = (2023, 11, 5)
    print(get_day_of_specific_date(*specific_sample_date))