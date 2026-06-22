from datetime import datetime

class DateConverter:
    def convert(self, date_object):
        return date_object.strftime('%A, %B %d, %Y')

if __name__ == '__main__':
    converter = DateConverter()
    sample_date1 = datetime(2021, 1, 1)
    print(converter.convert(sample_date1))
    sample_date2 = datetime(2023, 12, 31)
    print(converter.convert(sample_date2))