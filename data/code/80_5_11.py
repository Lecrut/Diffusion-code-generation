def compare_dates(date1, date2):
    return (date1 > date2) - (date1 < date2)
if __name__ == '__main__':
    print(compare_dates('2023-04-01', '2023-03-31'))
    print(compare_dates('2023-03-31', '2023-04-01'))
    print(compare_dates('2023-04-01', '2023-04-01'))