from datetime import datetime

def get_weekday(date_str):
    date_obj = datetime.strptime(date_str, '%B %d, %Y')
    weekday = date_obj.strftime('%A').upper()
    return weekday

if __name__ == '__main__':
    sample_date = 'July 4, 2024'
    print(get_weekday(sample_date))