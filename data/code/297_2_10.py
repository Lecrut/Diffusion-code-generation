class TimeConverter:

    def convert_seconds_to_hms(self, seconds):
        hours = seconds // 3600
        minutes = seconds % 3600 // 60
        remaining_seconds = seconds % 60
        return f'{hours:02}:{minutes:02}:{remaining_seconds:02}'
if __name__ == '__main__':
    converter = TimeConverter()
    print(converter.convert_seconds_to_hms(3661))
    print(converter.convert_seconds_to_hms(7322))