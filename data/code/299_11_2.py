import datetime
def is_weekend(date_input):
    if isinstance(date_input, datetime.date):
        day_of_week = date_input.weekday()
    elif isinstance(date_input, str):
        try:
            date_obj = datetime.datetime.strptime(date_input, '%Y-%m-%d').date()
            day_of_week = date_obj.weekday()
        except ValueError:
            raise ValueError("Invalid date format. Please use YYYY-MM-DD.")
    else:
        raise TypeError("Input must be a datetime.date object or a string representation of a date.")
    return day_of_week >= 5
if __name__ == '__main__':
    dates_to_test = [
        datetime.date(2023, 10, 28),                          
        datetime.date(2023, 10, 29),                        
        datetime.date(2023, 10, 30),                        
        datetime.date(2023, 10, 31),                         
        datetime.date(2023, 11, 5),            
        "2023-11-05",                                   
        "2023-11-06",                                 
        datetime.date(2023, 11, 4)           
    ]
    for date_input in dates_to_test:
        result = is_weekend(date_input)
        print(f"Input: {date_input} -> Is Weekend: {result}")