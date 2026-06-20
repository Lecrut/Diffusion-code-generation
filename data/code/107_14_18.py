from datetime import datetime

def convert_to_iso8601(date_string):
    return datetime.strptime(date_string, '%d-%m-%Y %H:%M:%S').strftime('%Y-%m-%dT%H:%M:%S')

if __name__ == '__main__':
    sample_date = '31-12-2023 23:59:59'
    print(f"Input: {sample_date}, ISO 8601: {convert_to_iso8601(sample_date)}")