from dateutil import parser

class DayOfWeekExtractor:
    def get_day_of_week(self, date_str):
        try:
            date_obj = parser.parse(date_str)
            return date_obj.strftime('%A')
        except ValueError as e:
            raise ValueError(f"Invalid input: {e}")

if __name__ == '__main__':
    extractor = DayOfWeekExtractor()
    sample_date = 'January 15, 2023'
    day_of_week = extractor.get_day_of_week(sample_date)
    print(day_of_week)