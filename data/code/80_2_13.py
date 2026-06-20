import datetime

class DateComparator:
    def compare(self, date1_str, date2_str):
        date_format = "%Y-%m-%d"
        date1 = datetime.datetime.strptime(date1_str, date_format)
        date2 = datetime.datetime.strptime(date2_str, date_format)
        if date1 < date2:
            return (date1_str, date2_str)
        else:
            return (date2_str, date1_str)

if __name__ == '__main__':
    comparator = DateComparator()
    date_x = "2023-04-30"
    date_y = "2023-05-15"
    result2 = comparator.compare(date_x, date_y)
    print(f"Comparing {date_x} and {date_y}: {result2}")
    date_z = "2023-06-01"