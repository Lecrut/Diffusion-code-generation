import datetime

def get_january_1_day():
    date = datetime.date(2024, 1, 1)
    return date.strftime("%A")

if __name__ == '__main__':
    result = get_january_1_day()
    print(result)