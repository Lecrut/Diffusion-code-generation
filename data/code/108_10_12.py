class DateResolver:
    TARGET_YEAR = 2024
    TARGET_MONTH = 1
    TARGET_DAY = 1

    @staticmethod
    def resolve_date(year, month, day):
        import datetime
        return datetime.date(year, month, day)

    @staticmethod
    def get_weekday_name(date_obj):
        import datetime
        mapping = {
            0: "Monday",
            1: "Tuesday",
            2: "Wednesday",
            3: "Thursday",
            4: "Friday",
            5: "Saturday",
            6: "Sunday"
        }
        return mapping[date_obj.weekday()]

if __name__ == '__main__':
    target_date = DateResolver.resolve_date(
        DateResolver.TARGET_YEAR,
        DateResolver.TARGET_MONTH,
        DateResolver.TARGET_DAY
    )
    weekday_name = DateResolver.get_weekday_name(target_date)
    print(weekday_name)