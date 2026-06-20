def weeks_difference(date1, date2):
    days_in_week = 7
    return abs((date2 - date1) // days_in_week)
if __name__ == '__main__':
    sample_date1 = 20230401
    sample_date2 = 20230501
    print(weeks_difference(sample_date1, sample_date2))