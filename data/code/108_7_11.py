class DateUtils:

    def __init__(self):
        self.days_in_month = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    def is_leap_year(self, year):
        return year % 4 == 0 and year % 100 != 0 or year % 400 == 0

    def set_leap_day(self):
        self.days_in_month[2] = 29

    def get_day_of_month(self, timestamp):
        seconds_per_day = 86400
        day_index = timestamp // seconds_per_day
        year = 1970 + day_index // 365 + day_index // 366
        day_of_year = day_index - (year - 1970) * 365 - (year - 1972) // 4 + (year - 1900) // 100 - (year - 1600) // 400
        if self.is_leap_year(year):
            day_of_year += 1
        return self.days_in_month[day_of_year % 12]
if __name__ == '__main__':
    utils = DateUtils()
    timestamp1 = 1709459200
    timestamp2 = 1672531200
    print(utils.get_day_of_month(timestamp1))
    print(utils.get_day_of_month(timestamp2))