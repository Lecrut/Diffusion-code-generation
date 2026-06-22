import datetime

def _get_iso_week_key(d: datetime.date) -> tuple:
    iso = d.isocalendar()
    return (iso[0], iso[1])

def same_iso_week(date_a: datetime.date, date_b: datetime.date) -> bool:
    return _get_iso_week_key(date_a) == _get_iso_week_key(date_b)

class WeekValidator:
    _MIN_DATE = datetime.date.min
    _MAX_DATE = datetime.date.max

    def __init__(self, d1: datetime.date, d2: datetime.date):
        self.d1 = d1
        self.d2 = d2

    def check(self) -> bool:
        return same_iso_week(self.d1, self.d2)

    @staticmethod
    def get_key(d: datetime.date) -> tuple:
        return _get_iso_week_key(d)

if __name__ == '__main__':
    date_x = datetime.date(2023, 1, 1)
    date_y = datetime.date(2023, 1, 7)
    date_z = datetime.date(2023, 1, 8)
    
    print(same_iso_week(date_x, date_y))
    print(same_iso_week(date_x, date_z))
    
    validator = WeekValidator(date_x, date_y)
    print(validator.check())
    
    print(WeekValidator.get_key(date_x))