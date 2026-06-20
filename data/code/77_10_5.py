class TimeConverter:
    def convert_to_total_minutes(self, time_str):
        try:
            hours, minutes, seconds = map(int, time_str.split(':'))
            total_minutes = hours * 60 + minutes + seconds / 60
            return int(total_minutes)
        except ValueError:
            raise ValueError("Invalid time format. Please use 'HH:MM:SS'.")

if __name__ == '__main__':
    converter = TimeConverter()
    try:
        print(converter.convert_to_total_minutes('1:30:45'))
    except ValueError as e:
        print(e)