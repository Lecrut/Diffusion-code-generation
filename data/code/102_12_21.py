import datetime

class DateVerifier:
    def __init__(self, date_input):
        if isinstance(date_input, str):
            try:
                self.date_obj = datetime.datetime.strptime(date_input, "%Y-%m-%d").date()
            except ValueError:
                raise ValueError(f"Invalid date string format: {date_input}")
        elif isinstance(date_input, datetime.date):
            self.date_obj = date_input
        else:
            raise ValueError(f"Unsupported type: {type(date_input)}")

    def is_weekday(self):
        return self.date_obj.weekday() < 5

    def is_weekend(self):
        return self.date_obj.weekday() >= 5

    def get_weekday_name(self):
        days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
        return days[self.date_obj.weekday()]

if __name__ == '__main__':
    verifier = DateVerifier("2023-10-07")
    print(verifier.is_weekday())
    print(verifier.get_weekday_name())
    print(verifier.is_weekend())