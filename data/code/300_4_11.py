import pandas as pd

class DateHandler:
    def __init__(self, date_str):
        self.date = pd.to_datetime(date_str)

    def remaining_days_in_month(self):
        end_of_month = pd.to_datetime(self.date).to_period('M').end_time
        return (end_of_month - self.date).days + 1

if __name__ == '__main__':
    sample_date = '2023-04-15'
    handler = DateHandler(sample_date)
    print(handler.remaining_days_in_month())