from datetime import datetime
from calendar import isleap

def get_day_of_month(dt: datetime) -> int:
    year = dt.year
    month = dt.month
    day = dt.day

    if month == 1:
        return day

    months_days = (0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)
    cumulative_days = [0]
    current_sum = 0
    for days in months_days:
        current_sum += days
        cumulative_days.append(current_sum)

    if isleap(year):
        cumulative_days[2] += 1
        cumulative_days[3] += 1
        cumulative_days[4] += 1
        cumulative_days[5] += 1
        cumulative_days[6] += 1
        cumulative_days[7] += 1
        cumulative_days[8] += 1
        cumulative_days[9] += 1
        cumulative_days[10] += 1
        cumulative_days[11] += 1
        cumulative_days[12] += 1

    start_of_year = datetime(year, 1, 1)
    day_of_year = (dt - start_of_year).days + 1
    
    previous_months_total = cumulative_days[month - 1]
    
    return day_of_year - previous_months_total

class DateAnalyzer:
    def __init__(self, dt: datetime):
        self.dt = dt

    def get_day(self) -> int:
        return get_day_of_month(self.dt)

    def get_month_name(self) -> str:
        months = (
            "January", "February", "March", "April", "May", "June",
            "July", "August", "September", "October", "November", "December"
        )
        return months[self.dt.month - 1]

if __name__ == '__main__':
    analyzer = DateAnalyzer(datetime(2024, 2, 29))
    print(analyzer.get_day())
    print(analyzer.get_month_name())