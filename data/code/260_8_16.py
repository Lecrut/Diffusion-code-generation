class DateComparator:
    DATE_FORMAT = "%Y-%m-%d"

    @staticmethod
    def parse_date(date_str):
        return datetime.strptime(date_str, DateComparator.DATE_FORMAT)

    @staticmethod
    def compare_dates(list1, list2):
        parsed_list1 = set(DateComparator.parse_date(date) for date in list1)
        parsed_list2 = set(DateComparator.parse_date(date) for date in list2)
        common_dates = parsed_list1.intersection(parsed_list2)
        return sorted(common_dates, reverse=True)

if __name__ == '__main__':
    dates1 = ["2023-04-01", "2023-05-15", "2023-06-20"]
    dates2 = ["2023-05-15", "2023-07-25", "2023-08-30"]
    result = DateComparator.compare_dates(dates1, dates2)
    print(result)