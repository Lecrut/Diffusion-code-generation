from datetime import datetime

def get_full_day_name(date_obj):
    return date_obj.strftime('%A')
if __name__ == '__main__':
    sample_date = datetime(2023, 9, 15)
    print(get_full_day_name(sample_date))