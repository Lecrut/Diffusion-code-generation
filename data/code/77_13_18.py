class TimeConverter:
    MINUTES_PER_HOUR = 60

    @staticmethod
    def convert_to_minutes(time_str):
        try:
            parts = time_str.split(':')
            if len(parts) != 2:
                raise ValueError("Incorrect format")
            hours, minutes = map(int, parts)
            if not (0 <= hours < 24 and 0 <= minutes < 60):
                raise ValueError("Time values out of range")
            total_minutes = (hours * TimeConverter.MINUTES_PER_HOUR) + minutes
            return total_minutes
        except ValueError as e:
            return f"Error: {e}"
        except Exception as e:
            return f"An unexpected error occurred: {e}"

if __name__ == '__main__':
    sample_input = "14:30"
    result = TimeConverter.convert_to_minutes(sample_input)
    print(result)