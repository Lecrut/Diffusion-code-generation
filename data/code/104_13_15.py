from datetime import datetime

class WeekChecker:
    DATE_FORMAT = '%Y-%m-%d'

    @staticmethod
    def dates_in_same_week(date1_str, date2_str):
        date1 = datetime.strptime(date1_str, WeekChecker.DATE_FORMAT)
        date2 = datetime.strptime(date2_str, WeekChecker.DATE_FORMAT)
        return date1.isocalendar()[1] == date2.isocalendar()[1]

if __name__ == '__main__':
    result1 = WeekChecker.dates_in_same_week('2023-10-01', '2023-10-07')
    print(f"Are '2023-10-01' and '2023-10-07' in the same week? {result1}")
    
    result2 = WeekChecker.dates_in_same_week('2023-10-01', '2023-10-08')
    print(f"Are '2023-10-01' and '2023-10-08' in the same week? {result2}")
    
    result3 = WeekChecker.dates_in_same_week('2023-10-07', '2023-10-01')
    print(f"Are '2023-10-07' and '2023-10-01' in the same week? {result3}")