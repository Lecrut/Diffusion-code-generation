class DateParser:
    @staticmethod
    def convert_date_string(date_string):
        try:
            date_obj = datetime.datetime.strptime(date_string, '%d-%b-%Y')
            return date_obj.strftime('%Y%m%d')
        except ValueError:
            return "Invalid Date Format"

if __name__ == '__main__':
    import datetime
    parser = DateParser()
    sample_date1 = '25-Jan-2023'
    sample_date2 = '15-Feb-2023'
    print(f"'{sample_date1}' converted: {parser.convert_date_string(sample_date1)}")
    print(f"'{sample_date2}' converted: {parser.convert_date_string(sample_date2)}")