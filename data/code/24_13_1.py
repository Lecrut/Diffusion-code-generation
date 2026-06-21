import calendar
from typing import final

@final
class LeapYearValidator:
    def __init__(self, year: int) -> None:
        self.year: int = year

    def is_leap(self) -> bool:
        return calendar.isleap(self.year)

if __name__ == '__main__':
    validator = LeapYearValidator(2000)
    print(validator.is_leap())
    
    validator2 = LeapYearValidator(1900)
    print(validator2.is_leap())
    
    validator3 = LeapYearValidator(2024)
    print(validator3.is_leap())
    
    validator4 = LeapYearValidator(2023)
    print(validator4.is_leap())