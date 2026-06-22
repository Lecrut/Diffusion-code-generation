from datetime import date, timedelta

def add_30_days():
    base_date = date(2024, 7, 4)
    result_date = base_date + timedelta(days=30)
    return result_date.strftime("%Y-%m-%d")

if __name__ == '__main__':
    print(add_30_days())