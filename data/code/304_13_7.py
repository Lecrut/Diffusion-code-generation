from datetime import datetime
class DateComparator:
    def is_before(self, date1: str, date2: str) -> bool:
        try:
            d1 = datetime.strptime(date1, '%Y-%m-%d')
            d2 = datetime.strptime(date2, '%Y-%m-%d')
            return d1 < d2
        except ValueError as e:
            raise ValueError(f"Invalid date format provided. Expected 'YYYY-MM-DD'. Error: {e}")
if __name__ == '__main__':
    comparator = DateComparator()
    date_a = "2023-01-15"
    date_b = "2023-01-20"
    date_c = "2023-01-15"
    date_d = "2023-01-15"
    date_e = "2023-02-01"
    print(f"Is {date_a} before {date_b}? {comparator.is_before(date_a, date_b)}")
    print(f"Is {date_b} before {date_a}? {comparator.is_before(date_b, date_a)}")
    print(f"Is {date_a} before {date_c}? {comparator.is_before(date_a, date_c)}")
    print(f"Is {date_d} before {date_a}? {comparator.is_before(date_d, date_a)}")
    print(f"Is {date_e} before {date_a}? {comparator.is_before(date_e, date_a)}")
    try:
        comparator.is_before("2023/01/01", "2023-01-15")
    except ValueError as e:
        print(f"Error caught for invalid format test: {e}")