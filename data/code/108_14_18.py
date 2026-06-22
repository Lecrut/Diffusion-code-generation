def get_day_of_month(date_obj):
    return date_obj.day

if __name__ == '__main__':
    class Date:
        def __init__(self, year, month, day):
            self.year = year
            self.month = month
            self.day = day

    sample_date = Date(2023, 10, 15)
    result = get_day_of_month(sample_date)
    print(result)