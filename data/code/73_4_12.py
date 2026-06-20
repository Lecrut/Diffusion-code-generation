from datetime import datetime

class DateDurationCalculator:
    FORMAT_SECONDS = 'seconds'
    FORMAT_HUMAN_READABLE = 'human_readable'

    @staticmethod
    def calculate_duration(start_date_str, end_date_str, format=FORMAT_SECONDS):
        start_date = datetime.strptime(start_date_str, '%Y-%m-%d %H:%M:%S')
        end_date = datetime.strptime(end_date_str, '%Y-%m-%d %H:%M:%S')
        duration = end_date - start_date
        if format == DateDurationCalculator.FORMAT_SECONDS:
            return duration.total_seconds()
        elif format == DateDurationCalculator.FORMAT_HUMAN_READABLE:
            days = duration.days
            hours = duration.seconds // 3600
            minutes = (duration.seconds // 60) % 60
            seconds = duration.seconds % 60
            return f'{days} days, {hours} hours'

if __name__ == '__main__':
    calculator = DateDurationCalculator()
    start_date = '2023-10-01 12:00:00'
    end_date = '2023-10-05 18:30:00'
    print(calculator.calculate_duration(start_date, end_date, format=DateDurationCalculator.FORMAT_HUMAN_READABLE))