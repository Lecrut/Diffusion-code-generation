from datetime import datetime
from typing import Union

class DateInspector:
    def __init__(self, reference_time: datetime) -> None:
        self.reference_time = reference_time

    def get_day_of_month(self) -> int:
        return self.reference_time.day

    def get_year(self) -> int:
        return self.reference_time.year

    def get_month(self) -> int:
        return self.reference_time.month

def extract_day(dt: datetime) -> int:
    inspector = DateInspector(dt)
    return inspector.get_day_of_month()

if __name__ == '__main__':
    sample_dt = datetime(2024, 12, 25, 8, 0, 0)
    day_value = extract_day(sample_dt)
    print(day_value)
    
    inspector_instance = DateInspector(sample_dt)
    print(inspector_instance.get_year())
    print(inspector_instance.get_month())