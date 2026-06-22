from datetime import datetime

def is_valid_date(date_str):
    try:
        datetime.strptime(date_str, '%d/%m/%Y %I:%M %p')
        return True
    except ValueError:
        return False

def convert_date_format(date_str):
    if not is_valid_date(date_str):
        raise ValueError("Invalid date format. Please use 'DD/MM/YYYY HH:MM AM/PM'.")
    
    dt_object = datetime.strptime(date_str, '%d/%m/%Y %I:%M %p')
    converted_date = dt_object.strftime('%Y-%m-%dT%H:%M:00')
    return converted_date

if __name__ == '__main__':
    sample_date = "15/08/2023 04:30 PM"
    try:
        result = convert_date_format(sample_date)
        print(result)
    except ValueError as e:
        print(e)