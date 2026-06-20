from datetime import date, timedelta

class DateSubtractor:
    MONTHS = 3
    
    def subtract_months(self, start_date):
        return start_date - timedelta(days=self.MONTHS * 30)

if __name__ == '__main__':
    subtractor = DateSubtractor()
    result = subtractor.subtract_months(date(2023, 10, 15))
    print(result)