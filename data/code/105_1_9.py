def first_sunday_after_jan_1():
    target_date = 2024
    month = 1
    day = 1
    
    while (month, day) != (1, 1):
        target_date += 1
    
    while True:
        if target_date % 7 == 6:
            return target_date
        target_date += 1

if __name__ == '__main__':
    print(first_sunday_after_jan_1())