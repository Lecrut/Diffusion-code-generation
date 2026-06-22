import datetime

class DateVerifier:
    def __init__(self, reference_date):
        if not isinstance(reference_date, datetime.date):
            raise ValueError("Expected a date object")
        self.reference_date = reference_date

    def is_weekday(self):
        return self.reference_date.weekday() < 5

    def get_weekday_name(self):
        days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
        return days[self.reference_date.weekday()]

if __name__ == '__main__':
    target_date = datetime.date(2023, 10, 23)
    verifier = DateVerifier(target_date)
    print(verifier.is_weekday())
    print(verifier.get_weekday_name())