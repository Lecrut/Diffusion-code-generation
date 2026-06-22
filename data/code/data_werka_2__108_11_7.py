from datetime import date

def get_day_of_month(d: date) -> int:
    return d.day

if __name__ == '__main__':
    target_date = date(2023, 3, 15)
    result = get_day_of_month(target_date)
    print(result)