from datetime import datetime, timedelta

def subtract_three_months(date_str):
    date_format = '%B %d, %Y'
    date_obj = datetime.strptime(date_str, date_format)
    new_date_obj = date_obj - timedelta(days=90)
    return new_date_obj.strftime(date_format)
if __name__ == '__main__':
    sample_date = 'October 15, 2023'
    result = subtract_three_months(sample_date)
    print(result)