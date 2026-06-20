class TimeConverter:
    @staticmethod
    def convert_to_minutes(time_str):
        parts = time_str.split(':')
        hours = int(parts[0])
        minutes = int(parts[1])
        seconds = int(parts[2])
        total_minutes = hours * 60 + minutes + seconds / 60.0
        return total_minutes

if __name__ == '__main__':
    converter = TimeConverter()
    print(converter.convert_to_minutes('1:30:00'))
    print(converter.convert_to_minutes('0:05:30'))
    print(converter.convert_to_minutes('2:15:45'))