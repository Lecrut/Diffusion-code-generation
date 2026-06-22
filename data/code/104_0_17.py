from datetime import datetime

class DateComparator:
    def __init__(self, ref_date: datetime, cmp_date: datetime):
        self.ref_date = ref_date
        self.cmp_date = cmp_date

    def is_first_earlier(self) -> bool:
        if self.ref_date.tzinfo is not None or self.cmp_date.tzinfo is not None:
            raise ValueError("Timezone-aware datetimes are not supported for direct comparison in this context")
        if self.ref_date == self.cmp_date:
            return False
        return self.ref_date < self.cmp_date

def compare_dates(d1: datetime, d2: datetime) -> bool:
    comp = DateComparator(d1, d2)
    return comp.is_first_earlier()

if __name__ == '__main__':
    first_dt = datetime(2023, 11, 15, 8, 30, 0)
    second_dt = datetime(2023, 11, 15, 9, 45, 0)
    print(compare_dates(first_dt, second_dt))
    print(compare_dates(second_dt, first_dt))
    print(compare_dates(first_dt, first_dt))