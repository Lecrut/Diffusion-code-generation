import datetime

class DateCalculator:
    TARGET_DAY = "Thursday"
    
    @staticmethod
    def calculate_next_thursday(start_date):
        target_day_index = datetime.datetime.strptime(DateCalculator.TARGET_DAY.lower(), "%A").weekday()
        start_weekday_index = start_date.weekday()
        days_until_target = (target_day_index - start_weekday_index) % 7
        return start_date + datetime.timedelta(days=days_until_target)

if __name__ == '__main__':
    sample_date_str = "2023-09-15"
    sample_date = datetime.datetime.strptime(sample_date_str, "%Y-%m-%d").date()
    next_thursday = DateCalculator.calculate_next_thursday(sample_date)
    print(next_thursday.strftime("%Y-%m-%d"))