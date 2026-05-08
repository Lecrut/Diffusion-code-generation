lambda dt: dt.day
if __name__ == '__main__':
    import datetime
    sample_date = datetime.datetime(2023, 10, 27, 14, 30, 0)
    result = (lambda dt: dt.day)(sample_date)
    print(result)