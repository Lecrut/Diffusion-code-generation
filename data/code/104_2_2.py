class DateComparator:
    def compare(self, date1_str, date2_str):
        date1 = datetime.datetime.strptime(date1_str, "%Y-%m-%d").date()
        date2 = datetime.datetime.strptime(date2_str, "%Y-%m-%d").date()
        if date1 < date2:
            return (date1, date2)
        elif date1 > date2:
            return (date2, date1)
        else:
            return (date1, date2)
if __name__ == '__main__':
    import datetime
    comparator = DateComparator()
    date1 = "2023-01-15"
    date2 = "2023-01-20"
    result1 = comparator.compare(date1, date2)
    print(result1)
    date3 = "2024-05-01"
    date4 = "2024-04-30"
    result2 = comparator.compare(date3, date4)
    print(result2)
    date5 = "2023-12-31"
    date6 = "2023-12-31"
    result3 = comparator.compare(date5, date6)
    print(result3)