import datetime

def calculate_remaining_days(target_month, target_year):
    try:
        current_date = datetime.date.today()
        if not (1 <= target_month <= 12) or target_year < current_date.year:
            raise ValueError("Invalid date input")
        
        next_month_start = datetime.date(target_year, target_month + 1, 1)
        if next_month_start.month == 1:
            days_in_target_month = (datetime.date(target_year + 1, 12, 31) - datetime.date(target_year, target_month, 1)).days
        else:
            days_in_target_month = (next_month_start - datetime.date(target_year, target_month, 1)).days
        
        if current_date.year == target_year and current_date.month > target_month:
            return days_in_target_month - (current_date.day - 1)
        return days_in_target_month

    except ValueError as e:
        print(e)

if __name__ == '__main__':
    target_month = 2
    target_year = 2024
    result = calculate_remaining_days(target_month, target_year)
    print(result)