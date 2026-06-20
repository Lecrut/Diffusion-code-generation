class TimeConverter:
    def convert_to_total_minutes(self, hours, minutes, seconds):
        return (hours * 60) + minutes + (seconds / 60)

if __name__ == '__main__':
    converter = TimeConverter()
    result = converter.convert_to_total_minutes(1, 30, 45)
    print(result)