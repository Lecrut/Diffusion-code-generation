class DateComparator:
    def is_before(self, date1_str, date2_str):
        try:
            date1 = datetime.strptime(date1_str, '%Y-%m-%d').date()
            date2 = datetime.strptime(date2_str, '%Y-%m-%d').date()
            return date1 < date2
        except ValueError:
            raise ValueError("Invalid date format. Please use YYYY-MM-DD.")
if __name__ == '__main__':
    from datetime import datetime
    comparator = DateComparator()
    date_str_1 = "2023-01-15"
    date_str_2 = "2023-02-20"
    result1 = comparator.is_before(date_str_1, date_str_2)
    print(f"Is {date_str_1} before {date_str_2}? {result1}")
    date_str_3 = "2024-05-01"
    date_str_4 = "2024-04-30"
    result2 = comparator.is_before(date_str_3, date_str_4)
    print(f"Is {date_str_3} before {date_str_4}? {result2}")
    date_str_5 = "2023-10-10"
    date_str_6 = "2023-10-10"
    result3 = comparator.is_before(date_str_5, date_str_6)
    print(f"Is {date_str_5} before {date_str_6}? {result3}")
    try:
        comparator.is_before("10/10/2023", "2023-01-01")
    except ValueError as e:
        print(f"Caught expected error for invalid input: {e}")