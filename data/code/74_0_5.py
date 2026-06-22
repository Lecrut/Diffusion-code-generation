import datetime
from enum import IntEnum

class DayOfWeek(IntEnum):
    MONDAY = 0
    TUESDAY = 1
    WEDNESDAY = 2
    THURSDAY = 3
    FRIDAY = 4
    SATURDAY = 5
    SUNDAY = 6

    @property
    def name_full(self):
        return self.name

    @property
    def abbreviation(self):
        return self.name[:3].upper()

def get_current_weekday():
    today = datetime.date.today()
    weekday_index = today.weekday()
    return DayOfWeek(weekday_index)

if __name__ == '__main__':
    current_day = get_current_weekday()
    print(current_day.name_full)
    print(current_day.value)
    print(current_day.abbreviation)