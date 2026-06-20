from datetime import datetime

def convert_date_string(date_str):
    try:
        date_obj = datetime.strptime(date_str, '%d-%b-%Y')
        return date_obj.strftime('%Y%m%d')
    except ValueError:
        raise ValueError("Invalid date format. Please use DD-Mon-YYYY.")

if __name__ == '__main__':
    sample_dates = ['25-Jan-2023', '15-Feb-2024', '01-Mar-2023']
    for date_str in sample_dates:
        print(f"'{date_str}' converted: {convert_date_string(date_str)}")