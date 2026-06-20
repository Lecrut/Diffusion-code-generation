class DateFormatConverter:
    INPUT_FORMAT = '%m/%d/%Y'
    OUTPUT_FORMAT = '%Y-%m-%d'

    @staticmethod
    def convert(date_str):
        return datetime.datetime.strptime(date_str, DateFormatConverter.INPUT_FORMAT).strftime(DateFormatConverter.OUTPUT_FORMAT)

if __name__ == '__main__':
    converter = DateFormatConverter()
    sample_date = "10/27/2023"
    result = converter.convert(sample_date)
    print(result)