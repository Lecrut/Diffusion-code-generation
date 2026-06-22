from datetime import datetime

def convert_datetime_to_string(date_obj):
    return date_obj.strftime('%A, %B %d, %Y')

if __name__ == '__main__':
    sample_date = datetime(2021, 1, 1)
    result = convert_datetime_to_string(sample_date)
    print(f"Input: {sample_date} -> Output: {result}")