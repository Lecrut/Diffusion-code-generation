from datetime import datetime

class DateConverter:
    ISO_FORMAT = '%Y-%m-%dT%H:%M:%S'
    INPUT_FORMAT = '%d-%m-%Y %H:%M:%S'

    @staticmethod
    def convert_to_iso(date_string):
        try:
            dt_object = datetime.strptime(date_string, DateConverter.INPUT_FORMAT)
            return dt_object.strftime(DateConverter.ISO_FORMAT)
        except ValueError:
            return None

if __name__ == '__main__':
    sample_date = '12-31-2023 23:59:59'
    converted_date = DateConverter.convert_to_iso(sample_date)
    print(f"Input: {sample_date}, Converted: {converted_date}")