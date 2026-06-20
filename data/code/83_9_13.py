from datetime import datetime

def are_dates_equal(date_str1: str, date_str2: str) -> bool:
    try:
        date1 = datetime.strptime(date_str1, '%Y-%m-%d')
        date2 = datetime.strptime(date_str2, '%Y-%m-%d')
        return date1 == date2
    except ValueError:
        return False
if __name__ == '__main__':
    print(are_dates_equal('2023-04-01', '2023-04-01'))
    print(are_dates_equal('2023-04-01', '2023-04-02'))
    print(are_dates_equal('2023-04-01', '2023/04/01'))