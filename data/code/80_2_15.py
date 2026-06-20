from datetime import datetime

class DateComparator:
    def compare(self, date1_str, date2_str):
        date1 = datetime.strptime(date1_str, '%Y-%m-%d')
        date2 = datetime.strptime(date2_str, '%Y-%m-%d')
        if date1 < date2:
            return (date1_str, date2_str)
        else:
            return (date2_str, date1_str)

if __name__ == '__main__':
    comparator = DateComparator()
    result = comparator.compare('2023-01-01', '2023-02-01')
    print(result)