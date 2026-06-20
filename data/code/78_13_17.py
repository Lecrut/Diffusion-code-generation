def month_difference(timestamp1, timestamp2):
    seconds_per_day = 86400
    days_per_year = 365

    year1, day_of_year1 = divmod(timestamp1 // seconds_per_day + 1970, days_per_year)
    month1, day_of_month1 = divmod(day_of_year1, 30)

    year2, day_of_year2 = divmod(timestamp2 // seconds_per_day + 1970, days_per_year)
    month2, day_of_month2 = divmod(day_of_year2, 30)

    if year1 != year2:
        return abs((year2 - year1) * 12 + month2 - month1)
    else:
        return abs(month2 - month1)

if __name__ == '__main__':
    print(month_difference(1633075200, 1645196800))