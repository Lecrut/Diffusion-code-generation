def extract_day_of_month(timestamp):
    days_in_month = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    is_leap = timestamp >> 16 & 1
    if is_leap:
        days_in_month[2] = 29
    month = timestamp >> 8 & 15
    return days_in_month[month]
if __name__ == '__main__':
    timestamp1 = 67108864
    print(extract_day_of_month(timestamp1))