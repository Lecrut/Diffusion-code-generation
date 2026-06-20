from datetime import datetime

def convert_to_iso(date_string):
    try:
        dt_object = datetime.strptime(date_string, '%d-%m-%Y %H:%M:%S')
        return dt_object.strftime('%Y-%m-%dT%H:%M:%S')
    except ValueError:
        return None

if __name__ == '__main__':
    sample_date = '15-04-2023 14:30:00'
    print(f"Input: {sample_date}, ISO: {convert_to_iso(sample_date)}")