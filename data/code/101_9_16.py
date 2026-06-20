from datetime import datetime

def get_day_of_week(date_str):
    try:
        date_obj = datetime.strptime(date_str, '%Y-%m-%d')
        return date_obj.strftime('%A').upper()
    except ValueError as e:
        return str(e)

if __name__ == '__main__':
    print(get_day_of_week('2023-11-11'))