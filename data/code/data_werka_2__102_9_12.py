import datetime

class DateValidator:
    def __init__(self, reference_date):
        if not isinstance(reference_date, datetime.date):
            raise ValueError("reference_date must be a datetime.date instance")
        self.reference_date = reference_date

    def is_weekday(self, target_date):
        if not isinstance(target_date, datetime.date):
            raise ValueError("target_date must be a datetime.date instance")
        return target_date.weekday() < 5

    def get_weekday_name(self, target_date):
        if not isinstance(target_date, datetime.date):
            raise ValueError("target_date must be a datetime.date instance")
        names = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
        return names[target_date.weekday()]

if __name__ == '__main__':
    validator = DateValidator(datetime.date(2023, 10, 1))
    dates_to_check = [
        datetime.date(2023, 10, 1),
        datetime.date(2023, 10, 2),
        datetime.date(2023, 10, 7),
        datetime.date(2023, 10, 8)
    ]
    results = []
    for d in dates_to_check:
        is_wd = validator.is_weekday(d)
        name = validator.get_weekday_name(d)
        results.append(f"{d.isoformat()}: {name} is weekday: {is_wd}")
    for line in results:
        print(line)