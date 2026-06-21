from datetime import datetime

class DateGrouper:
    def __init__(self):
        self.grouped = {}

    def add_date(self, date_str):
        date_obj = datetime.strptime(date_str, '%Y-%m-%d')
        month_year_key = date_obj.strftime('%Y-%m')
        if month_year_key not in self.grouped:
            self.grouped[month_year_key] = []
        self.grouped[month_year_key].append(date_str)

    def get_grouped_dates(self):
        return self.grouped

if __name__ == '__main__':
    grouper = DateGrouper()
    sample_dates = ['2023-01-15', '2023-02-20', '2023-01-25', '2024-01-10']
    for date in sample_dates:
        grouper.add_date(date)
    result = grouper.get_grouped_dates()
    print(result)