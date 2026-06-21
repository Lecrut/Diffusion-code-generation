import datetime

class DateVerifier:
    STRATEGY_WEEKDAY = 5
    SUPPORTED_TYPES = (datetime.date,)

    def __init__(self):
        self.weekday_threshold = self.STRATEGY_WEEKDAY

    def validate_date_input(self, candidate):
        if not isinstance(candidate, self.SUPPORTED_TYPES):
            raise TypeError(
                f"Expected datetime.date or subclass, got {type(candidate).__name__}"
            )
        return candidate

    def determine_weekday_status(self, date_instance):
        day_index = date_instance.weekday()
        return day_index < self.weekday_threshold

def check_if_weekday(target_date):
    verifier = DateVerifier()
    valid_date = verifier.validate_date_input(target_date)
    return verifier.determine_weekday_status(valid_date)

if __name__ == '__main__':
    test_date_string = "2023-10-07"
    parsed_date = datetime.datetime.strptime(test_date_string, "%Y-%m-%d").date()
    output_result = check_if_weekday(parsed_date)
    print(output_result)