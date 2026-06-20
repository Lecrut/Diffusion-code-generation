def weeks_between_julian_dates(julian_date1, julian_date2):
    return abs((julian_date2 - julian_date1) / 7)

if __name__ == '__main__':
    print(weeks_between_julian_dates(2459450.5, 2459523.5))