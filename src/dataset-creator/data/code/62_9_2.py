import threading
from datetime import date
def add_months(current_date: date, months_to_add: int) -> date:
    year = current_date.year + (months_to_add // 12)
    month = current_date.month - 1 + ((months_to_add % 12))
    while True:
        try:
            new_date = date(year, month, current_date.day)
            break
        except ValueError:
            if month < 1:
                month += 12
                year -= 1
            else:
                pass
    return new_date
def main():
    today = date.today()
    sample_months_to_add = 3
    result_date = add_months(today, sample_months_to_add)
    print(f"Original Date: {today}")
    print(f"Added Months: {sample_months_to_add}")
    print(f"Resulting Date: {result_date}")
if __name__ == '__main__':
    main()