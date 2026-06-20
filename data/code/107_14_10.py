from datetime import datetime

def convert_to_iso(date_str):
    return datetime.strptime(date_str, '%d-%m-%Y %H:%M:%S').isoformat()

if __name__ == '__main__':
    sample_date = '31-12-2023 23:59:59'
    print(convert_to_iso(sample_date))