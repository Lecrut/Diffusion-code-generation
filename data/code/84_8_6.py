from datetime import date

def day_of_year(input_date):
    return input_date.timetuple().tm_yday

if __name__ == '__main__':
    sample_date = date(2023, 4, 15)
    print(day_of_year(sample_date))