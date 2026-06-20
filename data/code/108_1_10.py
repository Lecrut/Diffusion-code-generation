class DateParser:
    MONTHS = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    @staticmethod
    def is_leap_year(year):
        return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

    @classmethod
    def determine_day(cls, timestamp):
        year = timestamp // 10000
        month = (timestamp % 10000) // 100
        day = timestamp % 100

        if month == 2 and cls.is_leap_year(year):
            cls.MONTHS[2] += 1

        return day

if __name__ == '__main__':
    parser = DateParser()
    timestamp1 = 20231027
    print(f"The day for {timestamp1} is: {parser.determine_day(timestamp1)}")
    timestamp2 = 19990101
    print(f"The day for {timestamp2} is: {parser.determine_day(timestamp2)}")
    timestamp3 = 20240229
    print(f"The day for {timestamp3} is: {parser.determine_day(timestamp3)}")