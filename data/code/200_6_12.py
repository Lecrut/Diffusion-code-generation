class DateMapper:
    def __init__(self):
        self.lookup = {
            '2023-04-01': 'Monday',
            '2023-04-02': 'Tuesday',
            '2023-04-03': 'Wednesday',
            '2023-04-04': 'Thursday',
            '2023-04-05': 'Friday'
        }

    def map_dates_to_days(self, dates):
        return [self.lookup.get(date, 'Unknown') for date in dates]

if __name__ == '__main__':
    mapper = DateMapper()
    sample_dates = ['2023-04-01', '2023-04-06', '2023-04-03']
    print(mapper.map_dates_to_days(sample_dates))