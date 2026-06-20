import datetime

class DayOfWeek:
    DAYS_OF_WEEK = {
        0: "Monday",
        1: "Tuesday",
        2: "Wednesday",
        3: "Thursday",
        4: "Friday",
        5: "Saturday",
        6: "Sunday"
    }

    @staticmethod
    def get_current_day_of_week():
        today = datetime.datetime.now()
        day_index = today.weekday()
        return DayOfWeek.DAYS_OF_WEEK[day_index]

if __name__ == '__main__':
    print(DayOfWeek.get_current_day_of_week())