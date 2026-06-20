class DateParser:
    MONTHS_DAYS = {1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30,
                   7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}

    @staticmethod
    def is_leap_year(year):
        return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

    @classmethod
    def get_day_of_month(cls, timestamp):
        year = timestamp // 10000
        month = (timestamp % 10000) // 100
        day = timestamp % 100
        if month == 2 and cls.is_leap_year(year):
            cls.MONTHS_DAYS[2] += 1
        return day

if __name__ == '__main__':
    parser = DateParser()
    timestamp1 = 20231027
    print(f"The day for {timestamp1} is: {parser.get_day_of_month(timestamp1)}")
    timestamp2 = 19990101
    print(f"The day for {timestamp2} is: {parser.get_day_of_month(timestamp2)}")
    timestamp3 = 20240229
    print(f"The day for {timestamp3} is: {parser.get_day_of_month(timestamp3)}")