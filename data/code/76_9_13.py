from datetime import datetime

def days_between(start_date_str, end_date_str):
    start_date = datetime.strptime(start_date_str, '%Y-%m-%d')
    end_date = datetime.strptime(end_date_str, '%Y-%m-%d')
    delta = end_date - start_date
    return delta.days

if __name__ == '__main__':
    sample_start_date = '2023-01-01'
    sample_end_date = '2023-01-31'
    print(days_between(sample_start_date, sample_end_date))