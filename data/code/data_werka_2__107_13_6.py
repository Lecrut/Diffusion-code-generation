import datetime

class DateFormatter:
    INPUT_FORMAT = '%Y/%m/%d'
    OUTPUT_FORMAT = '%B %d, %Y'

    @staticmethod
    def _parse(date_string):
        return datetime.datetime.strptime(date_string, DateFormatter.INPUT_FORMAT)

    @staticmethod
    def _format(date_obj):
        return date_obj.strftime(DateFormatter.OUTPUT_FORMAT)

    @classmethod
    def format(cls, date_string):
        parsed_date = cls._parse(date_string)
        return cls._format(parsed_date)

if __name__ == '__main__':
    sample_date = '2023/10/05'
    formatted_date = DateFormatter.format(sample_date)
    print(formatted_date)