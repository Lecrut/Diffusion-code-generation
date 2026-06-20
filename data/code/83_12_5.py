from datetime import datetime

def compare_dates(date_str1, date_str2):
    return datetime.strptime(date_str1, '%Y-%m-%d') < datetime.strptime(date_str2, '%Y-%m-%d')

if __name__ == '__main__':
    print(compare_dates('2023-04-01', '2023-04-02'))