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
import datetime
if __name__ == '__main__':
    comparator = DateComparator()
    date_a = "2023-01-15"
    date_b = "2023-01-20"
    print(f"Comparing {date_a} and {date_b}: {comparator.compare(date_a, date_b)}")
    date_c = "2024-05-01"
    date_d = "2024-04-30"
    print(f"Comparing {date_c} and {date_d}: {comparator.compare(date_c, date_d)}")
    date_e = "2023-12-31"
    date_f = "2023-12-31"
    print(f"Comparing {date_e} and {date_f}: {comparator.compare(date_e, date_f)}")