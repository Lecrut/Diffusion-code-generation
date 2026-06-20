from dateutil.relativedelta import relativedelta

def is_within_one_week(date_str1, date_str2):
    from_date = dateutil.parser.parse(date_str1)
    to_date = dateutil.parser.parse(date_str2)
    return abs(from_date - to_date) <= relativedelta(weeks=1)

if __name__ == '__main__':
    sample_date1 = '2023-10-26'
    sample_date2 = '2023-11-02'
    print(is_within_one_week(sample_date1, sample_date2))

    another_sample_date1 = '2024-01-01'
    another_sample_date2 = '2024-01-08'
    print(is_within_one_week(another_sample_date1, another_sample_date2))