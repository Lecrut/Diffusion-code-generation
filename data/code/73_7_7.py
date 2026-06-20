from datetime import datetime

def parse_date(date_str):
    return datetime.strptime(date_str, '%Y-%m-%d %H:%M:%S')

def date_difference(date1_str, date2_str):
    date1 = parse_date(date1_str)
    date2 = parse_date(date2_str)
    delta = abs(date2 - date1)
    return delta.total_seconds() / 60

if __name__ == '__main__':
    sample_dates = {
        'date_a': '2023-10-29 10:00:00',
        'date_b': '2023-11-02 14:30:00'
    }
    
    result = date_difference(sample_dates['date_a'], sample_dates['date_b'])
    print(f"Difference in minutes: {result}")