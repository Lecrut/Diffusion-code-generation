from datetime import datetime, timedelta

class DateCalculator:
    WEEKDAYS = {
        'monday': 0,
        'tuesday': 1,
        'wednesday': 2,
        'thursday': 3,
        'friday': 4,
        'saturday': 5,
        'sunday': 6,
    }

    @staticmethod
    def _parse_date(date_string):
        return datetime.strptime(date_string, '%Y-%m-%d')

    @staticmethod
    def _validate_weekday_name(weekday_name):
        if weekday_name not in DateCalculator.WEEKDAYS:
            raise ValueError(f"Invalid weekday name: {weekday_name}")
        return DateCalculator.WEEKDAYS[weekday_name]

    def find_next_weekday(self, start_date_str, target_weekday_name):
        start_date = self._parse_date(start_date_str)
        target_weekday = self._validate_weekday_name(target_weekday_name)
        
        current_weekday = start_date.weekday()
        days_difference = target_weekday - current_weekday
        
        if days_difference <= 0:
            days_difference += 7
            
        next_date = start_date + timedelta(days=days_difference)
        return next_date.strftime('%Y-%m-%d')

if __name__ == '__main__':
    calculator = DateCalculator()
    result = calculator.find_next_weekday('2023-10-01', 'friday')
    print(result)