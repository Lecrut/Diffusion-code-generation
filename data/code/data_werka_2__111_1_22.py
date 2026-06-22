from datetime import date, timedelta

def add_days_to_july_4():
    base_year = 2024
    base_month = 7
    base_day = 4
    days_to_add = 30
    
    start_date = date(base_year, base_month, base_day)
    result_date = start_date + timedelta(days=days_to_add)
    
    return result_date.strftime("%Y-%m-%d")

if __name__ == '__main__':
    print(add_days_to_july_4())