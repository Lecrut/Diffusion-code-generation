import datetime
import calendar

class DateAnalyzer:
    TARGET_DATE = datetime.date(2024, 7, 4)
    
    @staticmethod
    def analyze_date(target_date):
        if not isinstance(target_date, datetime.date):
            raise ValueError("Input must be a date object")
        weekday_index = target_date.weekday()
        weekday_name = calendar.day_name[weekday_index]
        return {
            'date': target_date,
            'weekday_index': weekday_index,
            'weekday_name': weekday_name
        }

if __name__ == '__main__':
    result = DateAnalyzer.analyze_date(DateAnalyzer.TARGET_DATE)
    print(result['weekday_name'])
    print(result['weekday_index'])
    print(result['date'])