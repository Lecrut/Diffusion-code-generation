import datetime

class DateUtil:
    DAYS_OF_WEEK = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

    @staticmethod
    def get_current_day():
        today = datetime.date.today()
        return DateUtil.DAYS_OF_WEEK[today.weekday()]

if __name__ == '__main__':
    current_day = DateUtil.get_current_day()
    print(current_day)