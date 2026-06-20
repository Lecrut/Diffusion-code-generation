import datetime

def calculate_remaining_time(target_month, target_day):
    today = datetime.date.today()
    year = today.year
    
    if target_month < today.month:
        target_month += 12
        year -= 1
    
    target_date = datetime.date(year, target_month, target_day)
    remaining_time = target_date - today
    
    return remaining_time

if __name__ == '__main__':
    target_month_1 = 10
    target_day_1 = 25
    result_1 = calculate_remaining_time(target_month_1, target_day_1)
    print(result_1)

    target_month_2 = 12
    target_day_2 = 31
    result_2 = calculate_remaining_time(target_month_2, target_day_2)
    print(result_2)