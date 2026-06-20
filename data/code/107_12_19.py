from datetime import datetime

class DateFormatConverter:
    INPUT_FORMAT = '%d-%b-%Y'
    OUTPUT_FORMAT = '%Y%m%d'

    @staticmethod
    def convert_date_string(date_string):
        try:
            date_obj = datetime.strptime(date_string, DateFormatConverter.INPUT_FORMAT)
            return date_obj.strftime(DateFormatConverter.OUTPUT_FORMAT)
        except ValueError:
            return "Invalid Date Format"

if __name__ == '__main__':
    sample_date1 = '25-Jan-2023'
    sample_date2 = '15-Feb-2024'
    sample_date3 = '31-Mar-2022'
    sample_date4 = 'not-a-date'

    converter = DateFormatConverter()
    print(f"'{sample_date1}' converted: {converter.convert_date_string(sample_date1)}")
    print(f"'{sample_date2}' converted: {converter.convert_date_string(sample_date2)}")
    print(f"'{sample_date3}' converted: {converter.convert_date_string(sample_date3)}")
    print(f"'{sample_date4}' converted: {converter.convert_date_string(sample_date4)}")