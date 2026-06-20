from datetime import date

def calculate_day_of_year(date_obj):
    return date_obj.timetuple().tm_yday

if __name__ == '__main__':
    sample_date = date(2023, 4, 15)
    print(calculate_day_of_year(sample_date))