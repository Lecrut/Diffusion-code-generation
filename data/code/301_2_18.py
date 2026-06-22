from datetime import datetime

class ISO8601Converter:
    OUTPUT_FORMAT = "%Y-%m-%dT%H:%M:%S.%f%z"

    @staticmethod
    def convert_to_iso(date_string):
        try:
            naive_datetime = datetime.strptime(date_string, '%Y-%m-%d')
            return naive_datetime.strftime(ISO8601Converter.OUTPUT_FORMAT)
        except ValueError:
            return "Error: Invalid input format. Expected YYYY-MM-DD."

if __name__ == '__main__':
    converter = ISO8601Converter()
    sample_date = "2023-10-27"
    print(converter.convert_to_iso(sample_date))