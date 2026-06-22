import datetime

class WeekComparator:
    def __init__(self, date1: datetime.date, date2: datetime.date):
        self.date1 = date1
        self.date2 = date2

    def is_same_week(self) -> bool:
        iso1 = self.date1.isocalendar()
        iso2 = self.date2.isocalendar()
        return iso1[:2] == iso2[:2]

    def get_week_info(self) -> dict:
        iso1 = self.date1.isocalendar()
        iso2 = self.date2.isocalendar()
        return {
            "date1": {"year": iso1[0], "week": iso1[1], "weekday": iso1[2]},
            "date2": {"year": iso2[0], "week": iso2[1], "weekday": iso2[2]}
        }

if __name__ == '__main__':
    d1 = datetime.date(2024, 1, 1)
    d2 = datetime.date(2024, 1, 5)
    d3 = datetime.date(2024, 1, 8)
    
    comp1 = WeekComparator(d1, d2)
    comp2 = WeekComparator(d1, d3)
    
    print(comp1.is_same_week())
    print(comp2.is_same_week())
    print(comp1.get_week_info())