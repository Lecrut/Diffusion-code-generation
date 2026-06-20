import calendar

class DateUtility:
    def days_left_in_month(self):
        today = datetime.date.today()
        _, days_in_month = calendar.monthrange(today.year, today.month)
        weekdays_count = sum(1 for day in range(1, days_in_month + 1) if (today.replace(day=day).weekday() < 5))
        return weekdays_count

if __name__ == '__main__':
    utility = DateUtility()
    weekday_count = utility.days_left_in_month()
    print(weekday_count)