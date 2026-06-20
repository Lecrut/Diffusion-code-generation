import datetime

class DateComparator:
    @staticmethod
    def compare_dates(date_str1, date_str2):
        try:
            date1 = datetime.datetime.strptime(date_str1, '%Y-%m-%d').date()
            date2 = datetime.datetime.strptime(date_str2, '%Y-%m-%d').date()
            if date1 < date2:
                return date1
            elif date2 < date1:
                return date2
            else:
                raise ValueError("Dates are the same")
        except ValueError as e:
            print(f"Error: {e}. Please use YYYY-MM-DD.")
            return None

if __name__ == '__main__':
    comparator = DateComparator()
    date1_input = "2023-10-25"
    date2_input = "2023-10-15"
    earlier_date = comparator.compare_dates(date1_input, date2_input)
    print(earlier_date)