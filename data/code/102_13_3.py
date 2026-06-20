from datetime import date

def is_weekday(date_obj):
    return 0 < date_obj.weekday() < 5
if __name__ == '__main__':
    sample_date = date(2023, 10, 16)
    print(is_weekday(sample_date))