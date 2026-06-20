from datetime import date

DAYS_PER_MONTH = 30

def days_between(start_date_str, end_date_str):
    start_date = date.fromisoformat(start_date_str)
    end_date = date.fromisoformat(end_date_str)
    return (end_date.year - start_date.year) * 12 + end_date.month - start_date.month + \
           max(0, min(DAYS_PER_MONTH, end_date.day) - max(1, start_date.day))

if __name__ == '__main__':
    print(days_between('2023-01-01', '2023-01-31'))