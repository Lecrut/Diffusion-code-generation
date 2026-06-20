def weeks_between_dates(date1, date2):
    import datetime
    delta = abs((datetime.datetime.strptime(date2, '%Y-%m-%d') - datetime.datetime.strptime(date1, '%Y-%m-%d')).days)
    return delta // 7

if __name__ == '__main__':
    print(weeks_between_dates('2023-01-01', '2023-01-08'))