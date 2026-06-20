from datetime import datetime

def convert_date_format(date_string):
    try:
        date_object = datetime.strptime(date_string, '%m/%d/%Y')
        return date_object.strftime('%d-%m-%Y')
    except ValueError:
        return "Invalid date format"

if __name__ == '__main__':
    sample_dates = {
        'MM/DD/YYYY': ['12/31/2023', '01/01/2024', '08/25/1999']
    }
    
    for original_format, dates in sample_dates.items():
        print(f"Original Format: {original_format}")
        for date_str in dates:
            converted_date = convert_date_format(date_str)
            print(f"{date_str} -> {converted_date}")