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
    print(f"Is 2023-01-01 before 2023-01-02? {comparator.is_before('2023-01-01', '2023-01-02')}")
    print(f"Is 2024-05-15 before 2024-05-15? {comparator.is_before('2024-05-15', '2024-05-15')}")
    print(f"Is 2023-12-31 before 2024-01-01? {comparator.is_before('2023-12-31', '2024-01-01')}")
    print(f"Is 2025-01-01 before 2023-12-31? {comparator.is_before('2025-01-01', '2023-12-31')}")
    try:
        comparator.is_before('2023/01/01', '2023-01-02')
    except ValueError as e:
        print(f"Error caught for invalid format: {e}")