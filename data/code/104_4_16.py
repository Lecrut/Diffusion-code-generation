def are_dates_equal(date1, date2):
    return date1 == date2

if __name__ == '__main__':
    sample_date1 = (2023, 10, 25)
    sample_date2 = (2023, 11, 15)
    
    result = are_dates_equal(sample_date1, sample_date2)
    print(result)