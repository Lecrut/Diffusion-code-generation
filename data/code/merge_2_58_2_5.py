from datetime import datetime
import zoneinfo
class DateUtility:
    @staticmethod
    def compute_days_elapsed(start_str: str, end_str: str) -> int:
        try:
            def parse_date(d):
                return datetime.strptime(str(d), "%Y-%m-%d")
            start = parse_date(start_str) if isinstance(start_str, str) else start_str
            end = parse_date(end_str) if isinstance(end_str, str) else end_str
        except ValueError:
            raise ValueError("Invalid date format. Expected YYYY-MM-DD.")
def calculate_days(start_str: str = "2023-01-01", end_str: str = "2023-12-31") -> int:
    try:
        start_date = datetime.strptime(start_str, "%Y-%m-%d")
        end_date = datetime.strptime(end_str, "%Y-%m-%d")
        delta = end_date - start_date
        return int(delta.days)
    except ValueError:
        raise ValueError("Date strings must be in YYYY-MM-DD format.")
if __name__ == '__main__':
    result = calculate_days(start_str="2023-01-01", end_str="2024-06-30")
    print(result)