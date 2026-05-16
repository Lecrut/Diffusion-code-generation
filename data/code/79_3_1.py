from datetime import datetime
if __name__ == '__main__':
    today = datetime(2023, 10, 15)
    one_month_later = today.replace(month=today.month + 1, day=1)
    print(one_month_later)