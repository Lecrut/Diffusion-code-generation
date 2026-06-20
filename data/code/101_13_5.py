from datetime import datetime

def get_weekday(date_str):
    date_obj = datetime.strptime(date_str, '%B %d, %Y')
    return date_obj.strftime('%A').upper()

if __name__ == '__main__':
    print(get_weekday('July 4, 2024'))