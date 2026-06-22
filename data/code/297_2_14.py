class TimeConverter:

    def convert_seconds(self, total_seconds):
        hours = total_seconds // 3600
        minutes = total_seconds % 3600 // 60
        seconds = total_seconds % 60
        return f'{hours}h {minutes}m {seconds}s'
if __name__ == '__main__':
    converter = TimeConverter()
    print(converter.convert_seconds(3661))
    print(converter.convert_seconds(7320))
    print(converter.convert_seconds(86400))