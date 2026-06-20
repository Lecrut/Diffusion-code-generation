from datetime import datetime

class DateFormatConverter:
    @staticmethod
    def convert(date_string):
        try:
            date_object = datetime.strptime(date_string, '%m/%d/%Y')
            return date_object.strftime('%d-%m-%Y')
        except ValueError:
            return "Invalid date format"

if __name__ == '__main__':
    converter = DateFormatConverter()
    date_str1 = "12/31/2023"
    date_str2 = "01/01/2024"
    date_str3 = "25/08/1999"
    print(converter.convert(date_str1))
    print(converter.convert(date_str2))
    print(converter.convert(date_str3))