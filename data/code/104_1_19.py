class DateComparator:
    DATE_FORMAT = "%Y-%m-%d"

    @staticmethod
    def compare_dates(date_str1, date_str2):
        dt1 = datetime.strptime(date_str1, DateComparator.DATE_FORMAT)
        dt2 = datetime.strptime(date_str2, DateComparator.DATE_FORMAT)
        if dt1 > dt2:
            return dt1.strftime(DateComparator.DATE_FORMAT)
        else:
            return dt2.strftime(DateComparator.DATE_FORMAT)

if __name__ == '__main__':
    comparator = DateComparator()
    date1 = "2023-10-26"
    date2 = "2023-10-25"
    result1 = comparator.compare_dates(date1, date2)
    print(result1)
    date3 = "2024-01-01"
    date4 = "2024-01-15"
    result2 = comparator.compare_dates(date3, date4)
    print(result2)