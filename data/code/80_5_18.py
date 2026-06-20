def compare_dates(date_str1, date_str2):
    DATE_FORMAT = '%Y-%m-%d'
    try:
        return (date_str1 > date_str2) - (date_str1 < date_str2)
    except ValueError:
        raise ValueError('Invalid date format. Please use YYYY-MM-DD.')
if __name__ == '__main__':
    print(compare_dates('2023-10-26', '2023-10-25'))
    print(compare_dates('2023-10-25', '2023-10-26'))
    print(compare_dates('2023-10-25', '2023-10-25'))