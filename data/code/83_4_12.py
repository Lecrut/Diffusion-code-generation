from datetime import date

class DateComparator:

    def __init__(self, date_str1: str, date_str2: str):
        self.date_obj1 = date.fromisoformat(date_str1)
        self.date_obj2 = date.fromisoformat(date_str2)

    def are_identical(self) -> bool:
        return self.date_obj1 == self.date_obj2
if __name__ == '__main__':
    comparator = DateComparator('2023-05-01', '2023-05-01')
    print(comparator.are_identical())