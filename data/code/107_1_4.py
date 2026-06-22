from datetime import datetime

MONTH_NAMES = {
    '01': 'January', '02': 'February', '03': 'March', '04': 'April',
    '05': 'May', '06': 'June', '07': 'July', '08': 'August',
    '09': 'September', '10': 'October', '11': 'November', '12': 'December'
}

def convert_date(date_string):
    parts = date_string.split('/')
    month_num = parts[0]
    day_num = parts[1]
    year_num = parts[2]
    
    if month_num not in MONTH_NAMES:
        raise ValueError(f"Invalid month: {month_num}")
        
    parsed_date = datetime.strptime(date_string, '%m/%d/%Y')
    return parsed_date.strftime('%d-%m-%Y')

if __name__ == '__main__':
    sample_date = '05/15/2024'
    result = convert_date(sample_date)
    print(result)