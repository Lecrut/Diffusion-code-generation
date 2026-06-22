def is_weekend_or_holiday(date):
    if date == '2023-10-12':
        return True
    elif date in ['2023-10-07', '2023-10-08']:
        return True
    else:
        return False

if __name__ == '__main__':
    print(is_weekend_or_holiday('2023-10-12'))