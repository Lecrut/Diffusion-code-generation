from datetime import datetime

class DateCalculator:
    SECONDS_PER_MINUTE = 60
    MINUTES_PER_HOUR = 60
    HOURS_PER_DAY = 24

    @staticmethod
    def calculate_duration(start_date_str, end_date_str, format='seconds'):
        start_date = datetime.strptime(start_date_str, '%Y-%m-%d %H:%M:%S')
        end_date = datetime.strptime(end_date_str, '%Y-%m-%d %H:%M:%S')
        duration = end_date - start_date
        if format == 'seconds':
            return duration.total_seconds()
        elif format == 'human_readable':
            days = duration.days
            hours = duration.seconds // (DateCalculator.SECONDS_PER_MINUTE * DateCalculator.MINUTES_PER_HOUR)
            minutes = (duration.seconds // DateCalculator.SECONDS_PER_MINUTE) % DateCalculator.MINUTES_PER_HOUR
            seconds = duration.seconds % DateCalculator.SECONDS_PER_MINUTE
            return f'{days} days, {hours} hours'

if __name__ == '__main__':
    calculator = DateCalculator()
    start_date = '2023-10-01 12:00:00'
    end_date = '2023-10-05 18:30:00'
    print(calculator.calculate_duration(start_date, end_date, format='human_readable'))