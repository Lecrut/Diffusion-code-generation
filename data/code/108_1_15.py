EPOCH = 19700101

def days_in_month(year, month):
    if month in {4, 6, 9, 11}:
        return 30
    elif month == 2:
        if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
            return 29
        else:
            return 28
    else:
        return 31

def determine_day(timestamp):
    days_since_epoch = timestamp - EPOCH
    month = 1
    while days_in_month(1970 + (days_since_epoch // 365), month) < days_since_epoch % 365:
        days_since_epoch -= days_in_month(1970 + (days_since_epoch // 365), month)
        month += 1
    return days_since_epoch % 365

if __name__ == '__main__':
    timestamp1 = 20231027
    print(f"The day for {timestamp1} is: {determine_day(timestamp1)}")
    timestamp2 = 19990101
    print(f"The day for {timestamp2} is: {determine_day(timestamp2)}")
    timestamp3 = 20240229
    print(f"The day for {timestamp3} is: {determine_day(timestamp3)}")