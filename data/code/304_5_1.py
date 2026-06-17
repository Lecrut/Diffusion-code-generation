from datetime import date
class DateComparator:
    def is_strictly_earlier(self, date1: date, date2: date) -> bool:
        return date1 < date2
if __name__ == '__main__':
    comparator = DateComparator()
    date_a = date(2023, 1, 1)
    date_b = date(2023, 1, 2)
    date_c = date(2023, 1, 1)
    print(f"Is {date_a} strictly earlier than {date_b}? {comparator.is_strictly_earlier(date_a, date_b)}")
    print(f"Is {date_b} strictly earlier than {date_a}? {comparator.is_strictly_earlier(date_b, date_a)}")
    print(f"Is {date_a} strictly earlier than {date_c}? {comparator.is_strictly_earlier(date_a, date_c)}")
    print(f"Is {date_c} strictly earlier than {date_a}? {comparator.is_strictly_earlier(date_c, date_a)}")