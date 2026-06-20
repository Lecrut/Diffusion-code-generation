from datetime import datetime

class DateConverter:
    def __init__(self):
        self.input_format = '%d-%m-%Y %H:%M:%S'

    def convert_to_iso(self, date_string):
        try:
            dt_object = datetime.strptime(date_string, self.input_format)
            return dt_object.strftime('%Y-%m-%dT%H:%M:%S')
        except ValueError:
            return None

if __name__ == '__main__':
    converter = DateConverter()
    sample_date = '31-12-2023 23:59:59'
    iso_date = converter.convert_to_iso(sample_date)
    print(f"Input: {sample_date}, ISO: {iso_date}")