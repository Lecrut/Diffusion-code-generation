from datetime import datetime

class DateFormatConverter:
    @staticmethod
    def convert(date_str):
        date_obj = datetime.strptime(date_str, '%Y-%m-%d')
        return date_obj.strftime('%d/%m/%Y')

if __name__ == '__main__':
    converter = DateFormatConverter()
    sample_date = '2023-12-31'
    converted_date = converter.convert(sample_date)
    print(converted_date)