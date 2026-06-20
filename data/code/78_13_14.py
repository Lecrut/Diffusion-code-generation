import math

def month_difference(timestamp1, timestamp2):
    year1 = timestamp1 // (365 * 24 * 60 * 60)
    year2 = timestamp2 // (365 * 24 * 60 * 60)
    month1 = timestamp1 % (365 * 24 * 60 * 60) // (30 * 24 * 60 * 60)
    month2 = timestamp2 % (365 * 24 * 60 * 60) // (30 * 24 * 60 * 60)
    return abs((year1 - year2) * 12 + month1 - month2)
if __name__ == '__main__':
    timestamp1 = 1672531200
    timestamp2 = 1640966400
    print(month_difference(timestamp1, timestamp2))