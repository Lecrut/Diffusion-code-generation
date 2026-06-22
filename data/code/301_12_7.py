from datetime import datetime

def datetime_to_string(date_obj):
    return date_obj.strftime('%A, %B %d, %Y')

if __name__ == '__main__':
    sample_date = datetime(2021, 1, 1)
    formatted_date = datetime_to_string(sample_date)
    print(formatted_date)