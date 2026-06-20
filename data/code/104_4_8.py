class DateComparator:
    DATE_FORMAT = '%Y-%m-%d'

    @staticmethod
    def is_same_date(date1, date2):
        try:
            return datetime.datetime.strptime(date1, DateComparator.DATE_FORMAT).date() == \
                   datetime.datetime.strptime(date2, DateComparator.DATE_FORMAT).date()
        except ValueError:
            raise ValueError("Invalid date format. Please use YYYY-MM-DD.")

if __name__ == '__main__':
    date_input1 = "2023-10-25"
    date_input2 = "2023-10-25"
    try:
        result = DateComparator.is_same_date(date_input1, date_input2)
        print(result)
    except ValueError as e:
        print(e)