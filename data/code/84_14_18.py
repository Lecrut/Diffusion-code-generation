import datetime

class DateHelper:
    @staticmethod
    def day_of_year(year, month, day):
        try:
            date_obj = datetime.date(year, month, day)
            return date_obj.timetuple().tm_yday
        except ValueError:
            return None

if __name__ == '__main__':
    sample_date = (2023, 10, 5)
    year, month, day = sample_date
    result = DateHelper.day_of_year(year, month, day)
    print(f"The day of the year for {year}-{month}-{day} is: {result}")