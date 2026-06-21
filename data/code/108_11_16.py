from datetime import date

def get_day_of_month(d):
    if not isinstance(d, date):
        raise ValueError("Expected date instance")
    return d.day

if __name__ == '__main__':
    target = date(2023, 3, 15)
    print(get_day_of_month(target))