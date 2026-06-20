from datetime import date

class DateComparator:

    def __init__(self, date_str1: str, date_str2: str):
        self.date1 = date.fromisoformat(date_str1)
        self.date2 = date.fromisoformat(date_str2)

    def are_identical(self) -> bool:
        return self.date1 == self.date2
if __name__ == '__main__':
    comparator1 = DateComparator('2023-01-01', '2023-01-01')
    print(comparator1.are_identical())
    comparator2 = DateComparator('2023-04-01', '2023-04-02')
    print(comparator2.are_identical())