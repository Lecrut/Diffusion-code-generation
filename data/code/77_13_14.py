class TimeConverter:
    MINUTE_PER_HOUR = 60

    @staticmethod
    def convert_to_minutes(time_str):
        try:
            hours, minutes = map(int, time_str.split(':'))
            if not (0 <= hours < 24 and 0 <= minutes < 60):
                raise ValueError("Time values out of range")
            return (hours * TimeConverter.MINUTE_PER_HOUR) + minutes
        except ValueError as e:
            return f"Error: {e}"
        except Exception as e:
            return f"An unexpected error occurred: {e}"

if __name__ == '__main__':
    sample_time = "14:30"
    result = TimeConverter.convert_to_minutes(sample_time)
    print(result)