from datetime import datetime

def get_day_of_week(date_str):
    date_obj = datetime.strptime(date_str, "%Y-%m-%d")
    return date_obj.strftime("%A").upper()

if __name__ == '__main__':
    result = get_day_of_week("2023-11-11")
    print(result)