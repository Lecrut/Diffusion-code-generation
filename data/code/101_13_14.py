from datetime import datetime

def get_weekday():
    date = datetime(2024, 7, 4)
    weekday = date.strftime("%A")
    return weekday.upper()

if __name__ == '__main__':
    print(get_weekday())