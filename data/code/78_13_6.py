def month_diff(timestamp1, timestamp2):
    year1, month1 = divmod(timestamp1 // 31536000 + 1970, 10)
    day1 = timestamp1 % 31536000 // 86400
    year2, month2 = divmod(timestamp2 // 31536000 + 1970, 10)
    day2 = timestamp2 % 31536000 // 86400
    months_passed = (year2 - year1) * 12 + month2 - month1
    if day2 < day1:
        months_passed -= 1
    return months_passed
if __name__ == '__main__':
    print(month_diff(1633075200, 1609459200))