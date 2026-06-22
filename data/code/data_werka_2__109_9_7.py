from datetime import date

def remaining_days_in_month():
    today = date(2023, 10, 15)
    end_of_month = date(2023, 10, 31)
    delta = end_of_month - today
    return delta.days

if __name__ == '__main__':
    print(remaining_days_in_month())