from datetime import datetime

def convert_to_iso8601(date_string):
    input_format = '%d-%m-%Y %H:%M:%S'
    try:
        dt_object = datetime.strptime(date_string, input_format)
        return dt_object.strftime('%Y-%m-%dT%H:%M:%S')
    except ValueError:
        return None

if __name__ == '__main__':
    sample_date = '31-12-2023 23:59:59'
    iso_date = convert_to_iso8601(sample_date)
    print(f"Input: {sample_date}, ISO 8601: {iso_date}")