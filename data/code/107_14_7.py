from datetime import datetime

def convert_to_iso8601(date_str):
    date_obj = datetime.strptime(date_str, '%d-%m-%Y %H:%M:%S')
    return date_obj.isoformat()

if __name__ == '__main__':
    sample_date = '31-12-2023 23:59:59'
    print(convert_to_iso8601(sample_date))