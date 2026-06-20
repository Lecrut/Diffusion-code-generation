def days_in_month(year):
    leap = year % 4 == 0 and year % 100 != 0 or year % 400 == 0
    return {1: 31, 2: 29 if leap else 28, 3: 31, 4: 30, 5: 31, 6: 30, 7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}

def epoch_to_day_of_month(epoch):
    import math
    sec_per_day = 86400
    day_index = math.floor(epoch / sec_per_day)
    base_day_index = 2 * 31 + 1 * 30 + 5 * 31 + 1
    total_days = day_index - base_day_index
    year, month, day = (1970, 1, 1)
    while True:
        if month == 2 and days_in_month(year)[2] != 28:
            max_days = 29
        else:
            max_days = days_in_month(year)[month]
        if total_days < max_days:
            day += total_days
            break
        else:
            total_days -= max_days
            month += 1
            if month > 12:
                month = 1
                year += 1
    return day
if __name__ == '__main__':
    epoch_timestamp = 1683459200
    print(epoch_to_day_of_month(epoch_timestamp))