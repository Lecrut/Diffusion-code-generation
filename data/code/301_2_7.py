class DateConverter:
    def convert(self, date_string, output_format):
        if output_format == 'DD-MM-YYYY':
            try:
                year, month, day = date_string.split('-')
                return f"{day}-{month}-{year}"
            except ValueError:
                return "Invalid input format for conversion"
        elif output_format == 'YYYY-MM-DD':
            if len(date_string) == 10 and date_string[4] == '-' and date_string[7] == '-':
                return date_string
            else:
                try:
                    from datetime import datetime
                    dt_obj = datetime.strptime(date_string, '%d-%m-%Y')
                    return dt_obj.strftime('%Y-%m-%d')
                except ValueError:
                    return "Invalid input format"
        else:
            return "Unsupported output format"
if __name__ == '__main__':
    converter = DateConverter()
    date_str_1 = "2023-10-27"
    format_1 = "DD-MM-YYYY"
    result_1 = converter.convert(date_str_1, format_1)
    print(f"Input: {date_str_1}, Format: {format_1} -> Result: {result_1}")
    date_str_2 = "27-10-2023"
    format_2 = "YYYY-MM-DD"
    result_2 = converter.convert(date_str_2, format_2)
    print(f"Input: {date_str_2}, Format: {format_2} -> Result: {result_2}")
    date_str_3 = "1999-01-01"
    format_3 = "YYYY-MM-DD"
    result_3 = converter.convert(date_str_3, format_3)
    print(f"Input: {date_str_3}, Format: {format_3} -> Result: {result_3}")
    date_str_4 = "2023/10/27"
    format_4 = "DD-MM-YYYY"
    result_4 = converter.convert(date_str_4, format_4)
    print(f"Input: {date_str_4}, Format: {format_4} -> Result: {result_4}")