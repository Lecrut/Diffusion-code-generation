from datetime import datetime
class DateComparator:
    def compare(self, date1_str, date2_str):
        date1 = datetime.strptime(date1_str, "%Y-%m-%d")
        date2 = datetime.strptime(date2_str, "%Y-%m-%d")
        if date1 < date2:
            return (date1_str, date2_str)
        elif date1 > date2:
            return (date2_str, date1_str)
        else:
            return (date1_str, date2_str)
if __name__ == '__main__':
    comparator = DateComparator()
    date_a = "2023-01-15"
    date_b = "2023-01-20"
    result1 = comparator.compare(date_a, date_b)
    print(result1)
    date_c = "2024-05-01"
    date_d = "2024-04-30"
    result2 = comparator.compare(date_c, date_d)
    print(result2)
    date_e = "2020-12-31"
    date_f = "2020-12-31"
    result3 = comparator.compare(date_e, date_f)
    print(result3)