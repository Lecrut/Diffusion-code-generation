from datetime import datetime
class DateConverter:
    def convert(self, date_string, input_format, output_format):
        try:
            date_object = datetime.strptime(date_string, input_format)
            converted_date = date_object.strftime(output_format)
            return converted_date
        except ValueError as e:
            return f"Error: Invalid date format or string provided. Details: {e}"
if __name__ == '__main__':
    converter = DateConverter()
    date_str_1 = "31-12-2023"
    input_format_1 = "%d-%m-%Y"
    output_format_1 = "%Y-%m-%d"
    result_1 = converter.convert(date_str_1, input_format_1, output_format_1)
    print(f"Input: {date_str_1} ({input_format_1}) -> Output: {result_1}")
    date_str_2 = "05/15/2024"
    input_format_2 = "%m/%d/%Y"
    output_format_2 = "%d-%m-%Y"
    result_2 = converter.convert(date_str_2, input_format_2, output_format_2)
    print(f"Input: {date_str_2} ({input_format_2}) -> Output: {result_2}")
    date_str_3 = "2025-01-20"
    input_format_3 = "%Y-%m-%d"
    output_format_3 = "%m/%d/%Y"
    result_3 = converter.convert(date_str_3, input_format_3, output_format_3)
    print(f"Input: {date_str_3} ({input_format_3}) -> Output: {result_3}")