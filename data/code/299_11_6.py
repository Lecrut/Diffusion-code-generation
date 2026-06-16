import datetime
def is_weekend(date_input):
    if isinstance(date_input, datetime.date):
        weekday = date_input.weekday()
    elif isinstance(date_input, str):
        try:
            date_obj = datetime.datetime.strptime(date_input, '%Y-%m-%d').date()
            weekday = date_obj.weekday()
        except ValueError:
            return False
    else:
        return False
    return weekday >= 5
if __name__ == '__main__':
    sample_dates = [
        datetime.date(2023, 10, 1),              
        datetime.date(2023, 10, 2),              
        datetime.date(2023, 10, 7),                
        datetime.date(2023, 10, 8),              
        "2023-10-01",                                 
        "2023-10-07",                                   
        datetime.date(2023, 10, 14)              
    ]
    for date_input in sample_dates:
        result = is_weekend(date_input)
        print(f"Input: {date_input} -> Is Weekend: {result}")