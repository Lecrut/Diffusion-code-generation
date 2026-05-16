def calculate_day_of_week(day, month):
    if month == 1:
        days_in_month = 31
    elif month == 2:
        days_in_month = 28
    elif month == 4:
        days_in_month = 30
    elif month == 6:
        days_in_month = 30
    elif month == 9:
        days_in_month = 30
    elif month == 11:
        days_in_month = 30
    elif month == 12:
        days_in_month = 31
    else:
        return "Invalid month"
    days_passed = 0
    if month == 2:
        days_passed = 31           
    elif month == 3:
        days_passed = 31 + 28                                 
    elif month == 4:
        days_passed = 31 + 28 + 31                     
    elif month == 5:
        days_passed = 31 + 28 + 31 + 30                         
    elif month == 6:
        days_passed = 31 + 28 + 31 + 30 + 31                               
    elif month == 7:
        days_passed = 31 + 28 + 31 + 30 + 31 + 30                                     
    elif month == 8:
        days_passed = 31 + 28 + 31 + 30 + 31 + 30 + 31                                           
    elif month == 9:
        days_passed = 31 + 28 + 31 + 30 + 31 + 30 + 31 + 31                                                 
    elif month == 10:
        days_passed = 31 + 28 + 31 + 30 + 31 + 30 + 31 + 31 + 30                                                       
    elif month == 11:
        days_passed = 31 + 28 + 31 + 30 + 31 + 30 + 31 + 31 + 30 + 31             
    elif month == 12:
        days_passed = 31 + 28 + 31 + 30 + 31 + 30 + 31 + 31 + 30 + 31 + 30             
    day_of_week = (day + days_passed - 1) % 7
    return day_of_week + 1
if __name__ == '__main__':
    print(calculate_day_of_week(1, 1))
    print(calculate_day_of_week(15, 3))
    print(calculate_day_of_week(1, 4))
    print(calculate_day_of_week(29, 2))
    print(calculate_day_of_week(1, 12))
    print(calculate_day_of_week(31, 12))