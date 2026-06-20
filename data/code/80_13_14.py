from datetime import datetime

def compare_dates(date1: str, date2: str) -> int:
    return (datetime.strptime(date1, '%Y-%m-%d') - datetime.strptime(date2, '%Y-%m-%d')).days
if __name__ == '__main__':
    print(compare_dates('2023-04-01', '2023-04-02'))
    print(compare_dates('2023-04-01', '2023-04-01'))
    print(compare_dates('2023-04-02', '2023-04-01'))