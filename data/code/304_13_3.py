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
    date_b = "2023-02-20"
    result1 = comparator.is_before(date_a, date_b)
    print(f"Is {date_a} before {date_b}? {result1}")
    date_c = "2024-05-01"
    date_d = "2024-05-01"
    result2 = comparator.is_before(date_c, date_d)
    print(f"Is {date_c} before {date_d}? {result2}")
    date_e = "2025-10-10"
    date_f = "2024-12-31"
    result3 = comparator.is_before(date_e, date_f)
    print(f"Is {date_e} before {date_f}? {result3}")
    date_g = "2023-12-31"
    date_h = "2024-01-01"
    result4 = comparator.is_before(date_g, date_h)
    print(f"Is {date_g} before {date_h}? {result4}")