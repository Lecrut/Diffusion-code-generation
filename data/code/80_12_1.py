class DateComparator:
    def compare(self, date1_str, date2_str):
        try:
            date1 = datetime.datetime.strptime(date1_str, '%Y-%m-%d').date()
            date2 = datetime.datetime.strptime(date2_str, '%Y-%m-%d').date()
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
    date_a = "2023-10-25"
    date_b = "2023-11-15"
    date_c = "2023-10-25"
    date_d = "2022-12-31"
    print(f"Comparing {date_a} and {date_b}: {comparator.compare(date_a, date_b)}")
    print(f"Comparing {date_b} and {date_a}: {comparator.compare(date_b, date_a)}")
    print(f"Comparing {date_c} and {date_a}: {comparator.compare(date_c, date_a)}")
    print(f"Comparing {date_d} and {date_a}: {comparator.compare(date_d, date_a)}")
    print(f"Comparing {date_a} and {date_c}: {comparator.compare(date_a, date_c)}")
    print(f"Comparing {date_b} and {date_d}: {comparator.compare(date_b, date_d)}")
    try:
        comparator.compare("2023/10/25", "2023-11-15")
    except ValueError as e:
        print(f"Error caught: {e}")