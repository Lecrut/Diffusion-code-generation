import datetime
class DateConverter:
    def convert(self, date_string, input_format, output_format):
        try:
            date_object = datetime.datetime.strptime(date_string, input_format)
            converted_date = date_object.strftime(output_format)
            return converted_date
        except ValueError as e:
            return f"Error: Invalid date format or string provided. Details: {e}"
if __name__ == '__main__':
    converter = DateConverter()
    date1 = "31-12-2023"
    input_format1 = "%d-%m-%Y"
    output_format1 = "%Y/%m/%d"
    result1 = converter.convert(date1, input_format1, output_format1)
    print(f"Input: {date1} ({input_format1}) -> Output: {result1}")
    date2 = "05/06/2024"
    input_format2 = "%m/%d/%Y"
    output_format2 = "%d-%b-%Y"
    result2 = converter.convert(date2, input_format2, output_format2)
    print(f"Input: {date2} ({input_format2}) -> Output: {result2}")
    date3 = "15-08-2022"
    input_format3 = "%d-%m-%Y"
    output_format3 = "%Y-%m-%d"
    result3 = converter.convert(date3, input_format3, output_format3)
    print(f"Input: {date3} ({input_format3}) -> Output: {result3}")