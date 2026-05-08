def calculate_day_of_week(day, month):
    if month == 1:
        days_in_month = 31
    elif month == 2:
        days_in_month = 28
    elif month == 3:
        days_in_month = 31
    elif month == 4:
        days_in_month = 30
    elif month == 5:
        days_in_month = 31
    elif month == 6:
        days_in_month = 30
    elif month == 7:
        days_in_month = 31
    elif month == 8:
        days_in_month = 31
    elif month == 9:
        days_in_month = 30
    elif month == 10:
        days_in_month = 31
    elif month == 11:
        days_in_month = 30
    elif month == 12:
        days_in_month = 31
    else:
        raise ValueError("Invalid month")
    days_passed = 0
    for m in range(1, month):
        if m == 2 and (day > 29):
            days_passed += 29
        elif m == 2:
            days_passed += 28
        else:
            days_passed += (31 if m in [1, 3, 5, 7, 8, 10, 12] else 30)
    total_days = days_passed + day
    remainder = total_days % 7
    days_of_week = {0: "Sunday", 1: "Monday", 2: "Tuesday", 3: "Wednesday", 4: "Thursday", 5: "Friday", 6: "Saturday"}
    return days_of_week[remainder]
if __name__ == '__main__':
    test_cases = [
        (1, 1),                                                      
        (15, 3),                       
        (29, 2),                                                                    
        (31, 12)                      
    ]
    for day, month in test_cases:
        result = calculate_day_of_week(day, month)
        print(f"Day: {day}, Month: {month} -> Day of the week: {result}")