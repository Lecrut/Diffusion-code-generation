def find_first_sunday():
    start_date = 2024
    month = 1
    day = 1
    
    while True:
        if (month == 1 and day <= 31) or \
           (month == 2 and day <= 29) or \
           (month == 3 and day <= 31) or \
           (month == 4 and day <= 30) or \
           (month == 5 and day <= 31) or \
           (month == 6 and day <= 30) or \
           (month == 7 and day <= 31) or \
           (month == 8 and day <= 31) or \
           (month == 9 and day <= 30) or \
           (month == 10 and day <= 31) or \
           (month == 11 and day <= 30) or \
           (month == 12 and day <= 31):
            if (start_date % 4 == 0 and start_date % 100 != 0) or (start_date % 400 == 0):
                leap_year = True
            else:
                leap_year = False
            
            if (month == 2 and day > 28) and not leap_year:
                day = 1
                month += 1
            elif day > 31:
                day = 1
                month += 1
            elif month > 12:
                break
            else:
                if (start_date % 4 == 0 and start_date % 100 != 0) or (start_date % 400 == 0):
                    leap_year = True
                else:
                    leap_year = False
                
                if month in [4, 6, 9, 11] and day > 30:
                    day = 1
                    month += 1
                elif month == 2 and day > 28 and not leap_year:
                    day = 1
                    month += 1
                elif month == 2 and day > 29 and leap_year:
                    day = 1
                    month += 1
                else:
                    break
        
        if (month == 1 and day == 1):
            start_date += 1
            month = 1
            day = 1
        
        if (start_date % 4 == 0 and start_date % 100 != 0) or (start_date % 400 == 0):
            leap_year = True
        else:
            leap_year = False
        
        if (month == 2 and day > 28) and not leap_year:
            day = 1
            month += 1
        elif day > 31:
            day = 1
            month += 1
        elif month > 12:
            break
        else:
            if (month == 4 or month == 6 or month == 9 or month == 11) and day > 30:
                day = 1
                month += 1
            elif month == 2 and day > 28 and not leap_year:
                day = 1
                month += 1
            elif month == 2 and day > 29 and leap_year:
                day = 1
                month += 1
            else:
                break
    
    return f"{start_date}-{month:02d}-{day:02d}"

if __name__ == '__main__':
    print(find_first_sunday())