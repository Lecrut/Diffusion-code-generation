import calendar
def is_valid_date(year, month, day):
    if not isinstance(year, int) or not isinstance(month, int) or not isinstance(day, int):
        return False
    if month < 1 or month > 12:
        return False
    if not (1 <= day <= 31):
        return False
    if calendar.isleap(year):
        if month == 2 and not (1 <= day <= 29):
            return False
        if month in [4, 6, 9, 11] and not (1 <= day <= 30):
            return False
    else:
        if month == 2 and not (1 <= day <= 28):
            return False
        if month in [4, 6, 9, 11] and not (1 <= day <= 30):
            return False
    return True
if __name__ == '__main__':
    test_dates = [
        (2023, 10, 26),         
        (2024, 2, 29),                   
        (2023, 2, 29),                            
        (2023, 4, 31),                                
        (2023, 13, 1),                  
        (2024, 1, 32),                
        (2024, 2, 30),                                           
        (2024, 2, 28)           
    ]
    for year, month, day in test_dates:
        result = is_valid_date(year, month, day)
        print(f"Date ({year}, {month}, {day}): {result}")