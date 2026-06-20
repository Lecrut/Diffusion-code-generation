from datetime import datetime

class DateCalculator:
    DATE_FORMAT = '%Y-%m-%d'

    @staticmethod
    def years_difference(date_str1: str, date_str2: str) -> int:
        try:
            date1 = datetime.strptime(date_str1, DateCalculator.DATE_FORMAT)
            date2 = datetime.strptime(date_str2, DateCalculator.DATE_FORMAT)
            return abs((date2 - date1).days // 365)
        except ValueError as e:
            print(f'Error parsing dates: {e}')
            return None

if __name__ == '__main__':
    sample_date1 = '2000-01-01'
    sample_date2 = '2023-04-10'
    result = DateCalculator.years_difference(sample_date1, sample_date2)
    print(result)