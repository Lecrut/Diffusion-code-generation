import datetime

class DateFormatter:
    INPUT_FORMAT = '%Y/%m/%d'
    OUTPUT_FORMAT = '%B %d, %Y'

    @staticmethod
    def parse(input_str):
        return datetime.datetime.strptime(input_str, DateFormatter.INPUT_FORMAT)

    @staticmethod
    def format(date_obj):
        return date_obj.strftime(DateFormatter.OUTPUT_FORMAT)

    @classmethod
    def transform(cls, input_str):
        parsed = cls.parse(input_str)
        return cls.format(parsed)

if __name__ == '__main__':
    sample_date = '2023/10/05'
    formatted = DateFormatter.transform(sample_date)
    print(formatted)