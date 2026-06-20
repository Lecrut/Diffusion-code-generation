from datetime import datetime

class DateComparator:

    def check_equality(self, date_str1: str, date_str2: str) -> bool:
        return datetime.strptime(date_str1, '%Y-%m-%d') == datetime.strptime(date_str2, '%Y-%m-%d')
if __name__ == '__main__':
    comparator = DateComparator()
    print(comparator.check_equality('2023-04-01', '2023-04-01'))
    print(comparator.check_equality('2023-04-01', '2023-04-02'))