from datetime import datetime

class TimeCalculator:
    def validate_input(self, input_value):
        if isinstance(input_value, str):
            try:
                return datetime.fromisoformat(input_value)
            except ValueError:
                raise ValueError("Invalid ISO 8601 format")
        elif isinstance(input_value, datetime):
            return input_value
        else:
            raise ValueError("Unsupported time input type")

    def diff(self, start_time, end_time):
        validated_start = self.validate_input(start_time)
        validated_end = self.validate_input(end_time)
        delta = abs(validated_end - validated_start)
        days = delta.days
        hours = delta.seconds // 3600
        return f'{days} days, {hours} hours'

if __name__ == '__main__':
    calculator = TimeCalculator()
    result = calculator.diff('2023-10-01T00:00:00', '2023-10-05T12:00:00')
    print(result)