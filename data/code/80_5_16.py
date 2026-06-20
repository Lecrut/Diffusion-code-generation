def compare_dates(date1, date2):
    return (date1 > date2) - (date1 < date2)
if __name__ == '__main__':
    print(compare_dates('2023-10-05', '2023-09-30'))
    print(compare_dates('2023-08-15', '2023-08-15'))
    print(compare_dates('2023-07-20', '2023-07-25'))