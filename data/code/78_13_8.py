def month_diff(timestamp1, timestamp2):
    year1, month1 = divmod(timestamp1 // 31536000 + 1970, 10)
    day1 = timestamp1 % 31536000 // 86400
    year2, month2 = divmod(timestamp2 // 31536000 + 1970, 10)
    day2 = timestamp2 % 31536000 // 86400
    if year1 != year2:
        return (year2 - year1) * 12 + month2 - month1
    else:
        return month2 - month1
if __name__ == '__main__':
    print(month_diff(1633075200, 1645190400))