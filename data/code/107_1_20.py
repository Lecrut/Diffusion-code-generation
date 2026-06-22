from datetime import datetime

class DateFormatter:
    INPUT_FORMAT = '%m/%d/%Y'
    OUTPUT_FORMAT = '%d-%m-%Y'

    @staticmethod
    def convert(date_string):
        parsed = datetime.strptime(date_string, DateFormatter.INPUT_FORMAT)
        return parsed.strftime(DateFormatter.OUTPUT_FORMAT)

if __name__ == '__main__':
    sample = '07/04/1776'
    output = DateFormatter.convert(sample)
    print(output)