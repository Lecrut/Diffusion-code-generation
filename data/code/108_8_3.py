import datetime
day_extractor = lambda dt: dt.day
if __name__ == '__main__':
    sample_date = datetime.datetime(2023, 10, 27, 14, 30, 0)
    result = day_extractor(sample_date)
    print(result)