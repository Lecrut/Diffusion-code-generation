from datetime import date

class DateComparator:
    def __init__(self, date_str1: str, date_str2: str):
        self.date1 = date.fromisoformat(date_str1)
        self.date2 = date.fromisoformat(date_str2)

    def are_identical(self) -> bool:
        return self.date1 == self.date2

if __name__ == '__main__':
    comparator = DateComparator('2023-05-15', '2023-05-15')
    print(comparator.are_identical())
    
    comparator = DateComparator('2023-05-16', '2023-05-17')
    print(comparator.are_identical())