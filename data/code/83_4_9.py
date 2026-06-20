import datetime

def dates_are_identical(date_str1, date_str2):
    return datetime.date.fromisoformat(date_str1) == datetime.date.fromisoformat(date_str2)
if __name__ == '__main__':
    print(dates_are_identical('2023-04-01', '2023-04-01'))
    print(dates_are_identical('2023-04-01', '2023-04-02'))