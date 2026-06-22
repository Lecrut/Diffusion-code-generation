from datetime import datetime

def date_range_difference(start_date_str, end_date_str):
    start_date = datetime.strptime(start_date_str, '%Y-%m-%d')
    end_date = datetime.strptime(end_date_str, '%Y-%m-%d')
    return (end_date - start_date).days

if __name__ == '__main__':
    print(date_range_difference('2023-01-01', '2023-01-31'))