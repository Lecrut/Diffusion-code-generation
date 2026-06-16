class DateComparator:
    def is_before(self, date1_str, date2_str):
        try:
            date1 = datetime.strptime(date1_str, '%Y-%m-%d')
            date2 = datetime.strptime(date2_str, '%Y-%m-%d')
            return date1 < date2
        except ValueError:
            raise ValueError("Invalid date format. Please use YYYY-MM-DD.")
if __name__ == '__main__':
    from datetime import datetime
    comparator = DateComparator()
    date_a = "2023-01-15"
    date_b = "2023-01-20"
    date_c = "2023-01-15"
    date_d = "2023-01-15"
    invalid_date = "2023/01/15"
    print(f"Is {date_a} before {date_b}? {comparator.is_before(date_a, date_b)}")
    print(f"Is {date_b} before {date_a}? {comparator.is_before(date_b, date_a)}")
    print(f"Is {date_a} before {date_c}? {comparator.is_before(date_a, date_c)}")
    print(f"Is {date_c} before {date_a}? {comparator.is_before(date_c, date_a)}")
    print(f"Is {date_a} before {date_d}? {comparator.is_before(date_a, date_d)}")
    try:
        comparator.is_before(date_a, invalid_date)
    except ValueError as e:
        print(f"Error caught for invalid date: {e}")
    try:
        comparator.is_before(invalid_date, date_b)
    except ValueError as e:
        print(f"Error caught for invalid date: {e}")