import datetime

def calculate_remaining_days():
    now = datetime.datetime(2023, 10, 15)
    end_of_month = datetime.datetime(2023, 10, 31)
    delta = end_of_month - now
    return delta.days

if __name__ == '__main__':
    result = calculate_remaining_days()
    print(result)