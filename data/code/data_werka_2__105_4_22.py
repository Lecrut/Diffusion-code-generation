from datetime import date, timedelta
import calendar

def find_nearest_upcoming_saturday(base_date: date) -> date:
    if not isinstance(base_date, date):
        raise ValueError("Input must be a date instance")
    
    days_in_month = calendar.monthrange(base_date.year, base_date.month)[1]
    potential_dates = [
        base_date + timedelta(days=i)
        for i in range(0, days_in_month + 1)
    ]
    
    saturdays = [d for d in potential_dates if d.weekday() == calendar.SATURDAY]
    
    future_saturdays = [s for s in saturdays if s >= base_date]
    
    if not future_saturdays:
        next_month = base_date.replace(day=1)
        next_month = next_month + timedelta(days=32)
        next_month = next_month.replace(day=1)
        return find_nearest_upcoming_saturday(next_month)
        
    return future_saturdays[0]

if __name__ == '__main__':
    start_date = date(2023, 11, 1)
    computed_result = find_nearest_upcoming_saturday(start_date)
    print(computed_result)