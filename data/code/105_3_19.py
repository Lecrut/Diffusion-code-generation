from datetime import date, timedelta

def next_15th_day_of_month():
    start_date = date(2023, 3, 3)
    current_year = start_date.year
    current_month = start_date.month
    
    while True:
        target_date = date(current_year, current_month, 15)
        if target_date > start_date:
            return target_date
        current_month += 1
        if current_month > 12:
            current_month = 1
            current_year += 1

if __name__ == '__main__':
    result = next_15th_day_of_month()
    print(result)