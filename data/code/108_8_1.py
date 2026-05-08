lambda dt: dt.day
if __name__ == '__main__':
    from datetime import datetime
    sample_date = datetime(2023, 10, 27)
    result = (lambda dt: dt.day)(sample_date)
    print(result)