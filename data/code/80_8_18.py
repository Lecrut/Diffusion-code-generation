from datetime import date

class DateComparison:

    @staticmethod
    def parse_date(date_str: str) -> date:
        return date.fromisoformat(date_str)

    @staticmethod
    def compare_dates(date1: date, date2: date) -> int:
        if date1 == date2:
            return 0
        elif date1 < date2:
            return -1
        else:
            return 1

    @staticmethod
    def format_date(date_obj: date, format_str: str='%Y-%m-%d') -> str:
        return date_obj.strftime(format_str)
if __name__ == '__main__':
    date1_str = '2023-10-26'
    date2_str = '2023-10-27'
    date1 = DateComparison.parse_date(date1_str)
    date2 = DateComparison.parse_date(date2_str)
    comparison_result = DateComparison.compare_dates(date1, date2)
    print(comparison_result)
    formatted_date1 = DateComparison.format_date(date1)
    print(formatted_date1)