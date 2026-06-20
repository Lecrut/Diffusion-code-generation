from datetime import datetime, timedelta

def subtract_three_months(date_str):
    date_format = '%Y-%m-%d'
    date_obj = datetime.strptime(date_str, date_format)
    new_date = date_obj - timedelta(days=90)
    return new_date.strftime(date_format)
if __name__ == '__main__':
    sample_date = '2023-10-15'
    result = subtract_three_months(sample_date)
    print(result)