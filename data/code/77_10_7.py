class TimeConverter:
    def validate_time_str(self, time_str):
        parts = time_str.split(':')
        if len(parts) != 3:
            return False
        for part in parts:
            if not part.isdigit():
                return False
        return True

    def convert_to_total_minutes(self, time_str):
        if not self.validate_time_str(time_str):
            raise ValueError("Invalid time format. Expected 'HH:MM:SS'")
        
        hours, minutes, seconds = map(int, time_str.split(':'))
        total_minutes = hours * 60 + minutes + seconds / 60
        return int(total_minutes)

if __name__ == '__main__':
    converter = TimeConverter()
    print(converter.convert_to_total_minutes('1:30:45'))