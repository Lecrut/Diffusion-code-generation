def calculate_day_of_year(days_since_epoch, epoch_start_day):
    day_of_year = (days_since_epoch - epoch_start_day) % 365
    if day_of_year < 0:
        day_of_year += 365
    return day_of_year
if __name__ == '__main__':
    days_passed = 1000
    epoch_start = 1                                    
    day = calculate_day_of_year(days_passed, epoch_start)
    print(day)