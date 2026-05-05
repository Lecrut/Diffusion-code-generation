class TimeConverter:
    def convert_to_total_minutes(self, time_tuple):
        hours, minutes, seconds = time_tuple
        total_minutes = hours * 60 + minutes + seconds / 60
        return total_minutes
if __name__ == '__main__':
    converter = TimeConverter()
    sample_time = (2, 30, 15)
    result = converter.convert_to_total_minutes(sample_time)
    print(result)