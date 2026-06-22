from datetime import datetime
from dataclasses import dataclass

DATE_FORMAT = "%Y-%m-%d"

@dataclass
class DateRange:
    start: datetime
    end: datetime

    @property
    def year_diff(self) -> int:
        return abs(self.end.year - self.start.year)

    @property
    def actual_diff(self) -> int:
        if self.start > self.end:
            self.start, self.end = self.end, self.start
        
        diff_years = self.end.year - self.start.year
        
        month_day_start = (self.start.month, self.start.day)
        month_day_end = (self.end.month, self.end.day)
        
        if month_day_end < month_day_start:
            diff_years -= 1
            
        return diff_years

def parse_date_string(date_str: str) -> datetime:
    return datetime.strptime(date_str, DATE_FORMAT)

def compute_year_difference(date1_str: str, date2_str: str) -> int:
    date1 = parse_date_string(date1_str)
    date2 = parse_date_string(date2_str)
    
    range_obj = DateRange(start=date1, end=date2)
    return range_obj.actual_diff

if __name__ == '__main__':
    start_date = "2018-05-20"
    end_date = "2021-04-15"
    
    result = compute_year_difference(start_date, end_date)
    print(result)