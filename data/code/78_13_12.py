def month_difference(timestamp1, timestamp2):
    year1, month1 = divmod(timestamp1 // 31536000 + 1970, 10)
    year2, month2 = divmod(timestamp2 // 31536000 + 1970, 10)
    return (year2 - year1) * 12 + month2 - month1
if __name__ == '__main__':
    print(month_difference(1633024800, 1609459200))