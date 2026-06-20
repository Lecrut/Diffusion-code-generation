from datetime import datetime, timedelta

def get_next_weekday(start_date_str, target_weekday):
    weekdays = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    
    if target_weekday not in weekdays:
        raise ValueError("Invalid weekday")
    
    start_date = datetime.strptime(start_date_str, "%Y-%m-%d").date()
    days_to_add = (weekdays.index(target_weekday) - start_date.weekday() + 7) % 7
    
    return (start_date + timedelta(days=days_to_add)).strftime("%Y-%m-%d")

if __name__ == '__main__':
    result = get_next_weekday("2023-10-01", "Friday")
    print(result)