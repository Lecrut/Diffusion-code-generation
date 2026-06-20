def is_same_date(date1, date2):
    return date1 == date2

if __name__ == '__main__':
    sample_date1 = (2023, 10, 25)
    sample_date2 = (2023, 10, 25)
    result = is_same_date(sample_date1, sample_date2)
    print(result)