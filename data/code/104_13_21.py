import datetime

class WeekValidator:
    _ISO_YEAR_INDEX = 0
    _ISO_WEEK_INDEX = 1

    @staticmethod
    def _get_iso_week_components(d: datetime.date) -> tuple:
        iso_data = d.isocalendar()
        return (iso_data[WeekValidator._ISO_YEAR_INDEX], iso_data[WeekValidator._ISO_WEEK_INDEX])

    @classmethod
    def is_same_week(cls, d1: datetime.date, d2: datetime.date) -> bool:
        return cls._get_iso_week_components(d1) == cls._get_iso_week_components(d2)

if __name__ == '__main__':
    date_a = datetime.date(2024, 1, 1)
    date_b = datetime.date(2024, 1, 7)
    date_c = datetime.date(2024, 1, 8)
    result_1 = WeekValidator.is_same_week(date_a, date_b)
    result_2 = WeekValidator.is_same_week(date_a, date_c)
    print(result_1)
    print(result_2)