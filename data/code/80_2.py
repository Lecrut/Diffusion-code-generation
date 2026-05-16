import datetime
class DateComparator:
    def compare(self, date1_str, date2_str):
        date1 = datetime.datetime.strptime(date1_str, "%Y-%m-%d")
        date2 = datetime.datetime.strptime(date2_str, "%Y-%m-%d")
        if date1 < date2:
            return (date1_str, date2_str)
        elif date1 > date2:
            return (date2_str, date1_str)
        else:
            return (date1_str, date2_str)
if __name__ == '__main__':
    comparator = DateComparator()
    date_a = "2023-01-15"
    date_b = "2023-01-01"
    result1 = comparator.compare(date_a, date_b)
    print(f"Comparing {date_a} and {date_b}: {result1}")
    date_c = "2024-05-20"
    date_d = "2024-05-10"
    result2 = comparator.compare(date_c, date_d)
    print(f"Comparing {date_c} and {date_d}: {result2}")
    date_e = "2020-12-31"
    date_f = "2020-12-31"
    result3 = comparator.compare(date_e, date_f)
    print(f"Comparing {date_e} and {date_f}: {result3}")