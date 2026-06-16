from datetime import datetime
class DateComparator:
    def is_before(self, date1: str, date2: str) -> bool:
        try:
            d1 = datetime.strptime(date1, '%Y-%m-%d')
            d2 = datetime.strptime(date2, '%Y-%m-%d')
            return d1 < d2
        except ValueError as e:
            raise ValueError(f"Invalid date format provided: {e}")
if __name__ == '__main__':
    comparator = DateComparator()
    date_a = "2023-01-15"
    date_b = "2023-01-20"
    date_c = "2023-01-15"
    date_d = "2023-01-15"
    date_e = "2023-02-01"
    result1 = comparator.is_before(date_a, date_b)
    print(f"Is {date_a} before {date_b}? {result1}")
    result2 = comparator.is_before(date_b, date_a)
    print(f"Is {date_b} before {date_a}? {result2}")
    result3 = comparator.is_before(date_a, date_c)
    print(f"Is {date_a} before {date_c}? {result3}")
    result4 = comparator.is_before(date_d, date_d)
    print(f"Is {date_d} before {date_d}? {result4}")
    result5 = comparator.is_before(date_a, date_e)
    print(f"Is {date_a} before {date_e}? {result5}")
    try:
        comparator.is_before("2023/01/15", date_b)
    except ValueError as e:
        print(f"Caught expected error for invalid format: {e}")