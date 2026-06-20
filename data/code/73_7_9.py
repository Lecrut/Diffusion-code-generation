import datetime

class DateDifference:
    def __init__(self, date_str1, date_str2):
        self.date1 = datetime.datetime.strptime(date_str1, "%Y-%m-%d %H:%M:%S")
        self.date2 = datetime.datetime.strptime(date_str2, "%Y-%m-%d %H:%M:%S")

    def calculate_difference(self):
        return abs((self.date2 - self.date1).total_seconds() / 60)

if __name__ == '__main__':
    diff_instance = DateDifference("2023-10-29 10:00:00", "2023-11-02 14:30:00")
    difference_in_minutes = diff_instance.calculate_difference()
    print(difference_in_minutes)