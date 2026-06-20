def julian_to_weeks(julian_date):
    return (julian_date - 2451545) / 7
if __name__ == '__main__':
    date1 = 2459455
    date2 = 2460320
    print(julian_to_weeks(date2) - julian_to_weeks(date1))