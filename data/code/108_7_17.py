class UnixEpochToDay:
    MAX_DAYS_IN_MONTH = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    @staticmethod
    def is_leap_year(year):
        return year % 4 == 0 and year % 100 != 0 or year % 400 == 0

    @classmethod
    def adjust_february(cls, year):
        if cls.is_leap_year(year):
            cls.MAX_DAYS_IN_MONTH[2] = 29

    @staticmethod
    def get_day_of_month(day_number, unix_timestamp):
        seconds_per_day = 86400
        day_offset = unix_timestamp // seconds_per_day
        adjusted_date = (day_offset + 719163) % 146097
        year = 1970
        while True:
            cls.adjust_february(year)
            if day_offset < sum(cls.MAX_DAYS_IN_MONTH[:13]):
                break
            day_offset -= sum(cls.MAX_DAYS_IN_MONTH[:13])
            year += 1
        return (year, adjusted_date % 365 + 1)
if __name__ == '__main__':
    unix_timestamp = 1704028800
    print(UnixEpochToDay.get_day_of_month(1, unix_timestamp))