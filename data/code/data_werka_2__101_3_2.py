from datetime import datetime

def get_weekday(date_str):
    return datetime.strptime(date_str, "%Y-%m-%d").strftime("%A")

if __name__ == '__main__':
    print(get_weekday("2023-12-25"))