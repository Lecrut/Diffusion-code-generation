class DateComparator:
    def compare(self, date1_str, date2_str):
        try:
            date1 = datetime.datetime.strptime(date1_str, "%Y-%m-%d").date()
            date2 = datetime.datetime.strptime(date2_str, "%Y-%m-%d").date()
            if date1 < date2:
                return (date1, date2)
            elif date1 > date2:
                return (date2, date1)
            else:
                return (date1, date2)
        except ValueError:
            raise ValueError("Invalid date format. Please use YYYY-MM-DD.")
if __name__ == '__main__':
    import datetime
    comparator = DateComparator()
    date_a = "2023-10-26"
    date_b = "2023-10-15"
    date_c = "2024-01-01"
    date_d = "2024-01-01"
    result1 = comparator.compare(date_a, date_b)
    print(f"Comparing {date_a} and {date_b}: {result1}")
    result2 = comparator.compare(date_c, date_a)
    print(f"Comparing {date_c} and {date_a}: {result2}")
    result3 = comparator.compare(date_d, date_d)
    print(f"Comparing {date_d} and {date_d}: {result3}")
    result4 = comparator.compare("2022-12-31", "2023-01-01")
    print(f"Comparing 2022-12-31 and 2023-01-01: {result4}")