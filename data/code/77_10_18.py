class TimeConverter:
    @staticmethod
    def _parse_time(time_str):
        hours, minutes, seconds = map(int, time_str.split(':'))
        return hours, minutes, seconds

    def convert_to_total_minutes(self, time_str):
        hours, minutes, seconds = self._parse_time(time_str)
        total_minutes = hours * 60 + minutes + seconds / 60
        return int(total_minutes)

if __name__ == '__main__':
    converter = TimeConverter()
    print(converter.convert_to_total_minutes('1:30:45'))