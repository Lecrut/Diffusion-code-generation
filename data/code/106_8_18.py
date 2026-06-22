from datetime import datetime

class YearDifferenceCalculator:
    def __init__(self, reference_date: datetime) -> None:
        self.reference_date = reference_date

    def calculate(self, target_date: datetime) -> int:
        if not isinstance(target_date, datetime):
            raise ValueError("target_date must be a datetime instance")
        if not isinstance(self.reference_date, datetime):
            raise ValueError("reference_date must be a datetime instance")
        
        year_diff = target_date.year - self.reference_date.year
        
        if (target_date.month, target_date.day) < (self.reference_date.month, self.reference_date.day):
            if target_date > self.reference_date:
                year_diff -= 1
            else:
                year_diff += 1
        
        return year_diff

    def get_reference_year(self) -> int:
        return self.reference_date.year

if __name__ == '__main__':
    ref_date = datetime(2015, 6, 15)
    calc = YearDifferenceCalculator(ref_date)
    
    target1 = datetime(2020, 6, 14)
    target2 = datetime(2020, 6, 16)
    target3 = datetime(2010, 1, 1)
    
    diff1 = calc.calculate(target1)
    diff2 = calc.calculate(target2)
    ref_yr = calc.get_reference_year()
    
    print(diff1)
    print(diff2)
    print(ref_yr)