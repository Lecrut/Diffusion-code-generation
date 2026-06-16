from datetime import datetime
class DateConverter:
    def convert(self, date_string, input_format, output_format):
        try:
            date_object = datetime.strptime(date_string, input_format)
            converted_date = date_object.strftime(output_format)
            return converted_date
        except ValueError as e:
            return f"Error: Invalid date format or string: {e}"
if __name__ == '__main__':
    converter = DateConverter()
    date_str1 = "31-12-2023"
    input_format1 = "%d-%m-%Y"
    output_format1 = "%Y/%m/%d"
    result1 = converter.convert(date_str1, input_format1, output_format1)
    print(f"Input: {date_str1} ({input_format1}) -> Output: {result1}")
    date_str2 = "05/15/2024"
    input_format2 = "%m/%d/%Y"
    output_format2 = "%d-%b-%Y"
    result2 = converter.convert(date_str2, input_format2, output_format2)
    print(f"Input: {date_str2} ({input_format2}) -> Output: {result2}")
    date_str3 = "2025-01-01"
    input_format3 = "%Y-%m-%d"
    output_format3 = "%m/%d/%y"
    result3 = converter.convert(date_str3, input_format3, output_format3)
    print(f"Input: {date_str3} ({input_format3}) -> Output: {result3}")