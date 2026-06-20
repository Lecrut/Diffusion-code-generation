class TimeConverter:
    MINUTE_SECONDS = 60

    @staticmethod
    def calculate_total_minutes(time_str):
        try:
            parts = time_str.split(':')
            if len(parts) != 3:
                raise ValueError("Incorrect number of time components")
            hours = int(parts[0])
            minutes = int(parts[1])
            seconds = int(parts[2])
            total_seconds = hours * TimeConverter.MINUTE_SECONDS**2 + minutes * TimeConverter.MINUTE_SECONDS + seconds
            return total_seconds // TimeConverter.MINUTE_SECONDS
        except ValueError as ve:
            print(f"Error: {ve}")
            return None
        except Exception as e:
            print(f"Error: An unexpected error occurred")
            return None

if __name__ == '__main__':
    time1 = "1:30:00"
    time2 = "23:59:59"

    converter = TimeConverter()
    print(converter.calculate_total_minutes(time1))
    print(converter.calculate_total_minutes(time2))