class DateConverter:
    def convert(self, date_string, output_format):
        if output_format == 'DD-MM-YYYY':
            try:
                year, month, day = date_string.split('-')
                return f"{day}-{month}-{year}"
            except ValueError:
                return "Invalid input format for conversion."
        elif output_format == 'YYYY-MM-DD':
            if len(date_string) == 10 and date_string[4] == '-' and date_string[7] == '-':
                return date_string
            else:
                return "Input string does not match expected YYYY-MM-DD structure."
        else:
            return "Unsupported output format. Supported formats are 'YYYY-MM-DD' and 'DD-MM-YYYY'."
if __name__ == '__main__':
    converter = DateConverter()
    date1 = "2023-10-27"
    format1 = "DD-MM-YYYY"
    result1 = converter.convert(date1, format1)
    print(f"Input: {date1}, Format: {format1} -> Output: {result1}")
    date2 = "27-10-2023"
    format2 = "YYYY-MM-DD"
    result2 = converter.convert(date2, format2)
    print(f"Input: {date2}, Format: {format2} -> Output: {result2}")
    date3 = "2023/10/27"
    format3 = "DD-MM-YYYY"
    result3 = converter.convert(date3, format3)
    print(f"Input: {date3}, Format: {format3} -> Output: {result3}")
    date4 = "1999-01-01"
    format4 = "YYYY-MM-DD"
    result4 = converter.convert(date4, format4)
    print(f"Input: {date4}, Format: {format4} -> Output: {result4}")