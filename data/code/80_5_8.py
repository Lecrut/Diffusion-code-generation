class DateComparator:
    def compare_dates(self, date_str1, date_str2):
        if date_str1 > date_str2:
            return f"{date_str1} is after {date_str2}"
        elif date_str1 < date_str2:
            return f"{date_str1} is before {date_str2}"
        else:
            return f"{date_str1} is the same as {date_str2}"

if __name__ == '__main__':
    comparator = DateComparator()
    result1 = comparator.compare_dates('2023-10-26', '2023-10-25')
    print(result1)
    result2 = comparator.compare_dates('2023-01-15', '2023-01-15')
    print(result2)