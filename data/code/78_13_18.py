def month_difference(timestamp1, timestamp2):
    year1 = timestamp1 // (3600 * 24 * 365)
    month1 = timestamp1 % (3600 * 24 * 365) // (3600 * 24 * 30)
    year2 = timestamp2 // (3600 * 24 * 365)
    month2 = timestamp2 % (3600 * 24 * 365) // (3600 * 24 * 30)
    return (year2 - year1) * 12 + (month2 - month1)
if __name__ == '__main__':
    print(month_difference(1672531200, 1640966400))