def month_difference(timestamp1, timestamp2):
    year1 = timestamp1 // 31536000 + 1970
    month1 = (timestamp1 % 31536000) // 2592000 + 1
    year2 = timestamp2 // 31536000 + 1970
    month2 = (timestamp2 % 31536000) // 2592000 + 1
    if year1 != year2:
        return abs((year2 - year1) * 12 + month2 - month1)
    else:
        return abs(month2 - month1)

if __name__ == '__main__':
    print(month_difference(1633075200, 1645196800))