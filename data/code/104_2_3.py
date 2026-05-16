class DateComparator:
    def compare(self, date1_str, date2_str):
        from datetime import datetime
        date1 = datetime.strptime(date1_str, "%Y-%m-%d")
        date2 = datetime.strptime(date2_str, "%Y-%m-%d")
        if date1 < date2:
            return (date1, date2)
        elif date1 > date2:
            return (date2, date1)
        else:
            return (date1, date2)
if __name__ == '__main__':
    comparator = DateComparator()
    date_a = "2023-01-15"
    date_b = "2023-01-10"
    result1 = comparator.compare(date_a, date_b)
    print(result1)
    date_c = "2024-05-20"
    date_d = "2024-05-20"
    result2 = comparator.compare(date_c, date_d)
    print(result2)
    date_e = "2022-12-31"
    date_f = "2023-01-01"
    result3 = comparator.compare(date_e, date_f)
    print(result3)