from datetime import datetime

def validate_date(date_str):
    try:
        datetime.strptime(date_str, '%m/%d/%Y')
        return True
    except ValueError:
        return False

def convert_date(date_str):
    return date_str.replace('/', '-')

def format_dates(date_list):
    if not all(validate_date(date) for date in date_list):
        raise ValueError("All dates must be in 'MM/DD/YYYY' format")
    
    return [convert_date(date) for date in date_list]

if __name__ == '__main__':
    sample_dates = ['12/31/2020', '01/01/2021', '07/4/2022']
    formatted_dates = format_dates(sample_dates)
    print(formatted_dates)