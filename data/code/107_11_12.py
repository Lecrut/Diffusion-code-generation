class DateFormatter:
    INPUT_FORMAT = '%m/%d/%Y'
    OUTPUT_FORMAT = '%Y-%m-%d'

    @staticmethod
    def format_date_string(date_str):
        dt_object = datetime.datetime.strptime(date_str, DateFormatter.INPUT_FORMAT)
        return dt_object.strftime(DateFormatter.OUTPUT_FORMAT)

if __name__ == '__main__':
    sample_date = "10/27/2023"
    result = DateFormatter.format_date_string(sample_date)
    print(result)