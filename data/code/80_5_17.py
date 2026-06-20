class DateComparator:
    DATE_FORMAT = '%Y-%m-%d'

    @staticmethod
    def compare_dates(date_str1, date_str2):
        try:
            if date_str1 > date_str2:
                return f"{date_str1} is after {date_str2}"
            elif date_str1 < date_str2:
                return f"{date_str1} is before {date_str2}"
            else:
                return f"{date_str1} is the same as {date_str2}"
        except ValueError:
            return "Error: Invalid date format. Please use YYYY-MM-DD."

if __name__ == '__main__':
    comparator = DateComparator()
    result = comparator.compare_dates("2023-10-26", "2023-10-25")
    print(result)