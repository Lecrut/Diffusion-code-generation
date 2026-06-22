from datetime import datetime

def date_to_string(date_obj):
    return date_obj.strftime('%A, %B %d, %Y')

if __name__ == '__main__':
    sample_date = datetime(2021, 1, 1)
    result = date_to_string(sample_date)
    print(f"Date: {sample_date} -> String: {result}")