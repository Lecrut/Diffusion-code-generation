from datetime import date

def is_weekday(d):
    return d.weekday() < 5

if __name__ == '__main__':
    sample_date = date(2023, 10, 23)
    print(is_weekday(sample_date))