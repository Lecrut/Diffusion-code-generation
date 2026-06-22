from datetime import datetime

def iso8601_format(date_string):
    try:
        date_obj = datetime.strptime(date_string, '%Y-%m-%d')
        return date_obj.strftime('%Y-%m-%dT%H:%M:%S.%f%z')
    except ValueError:
        return "Error: Invalid input format. Expected YYYY-MM-DD."

if __name__ == '__main__':
    sample_date = "2023-11-15"
    print(iso8601_format(sample_date))