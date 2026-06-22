from datetime import datetime

def convert_to_iso8601(date_string):
    try:
        dt = datetime.strptime(date_string, '%Y-%m-%d')
        return dt.strftime('%Y-%m-%dT%H:%M:%S.%f%z')
    except ValueError:
        return "Error: Invalid input format. Expected YYYY-MM-DD."

if __name__ == '__main__':
    sample_date = "2023-10-27"
    print(convert_to_iso8601(sample_date))