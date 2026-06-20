from datetime import datetime

def convert_date_format(date_str):
    try:
        date_obj = datetime.strptime(date_str, '%d-%b-%Y')
        return date_obj.strftime('%Y%m%d')
    except ValueError:
        return "Invalid Date Format"

if __name__ == '__main__':
    sample_date1 = '25-Jan-2023'
    sample_date2 = '15-Feb-2024'
    print(f"'{sample_date1}' converted: {convert_date_format(sample_date1)}")
    print(f"'{sample_date2}' converted: {convert_date_format(sample_date2)}")