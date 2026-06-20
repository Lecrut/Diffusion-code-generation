DATE_FORMAT_INPUT = '%m/%d/%Y'
DATE_FORMAT_OUTPUT = '%Y-%m-%d'

def convert_date_format(date_str):
    return datetime.datetime.strptime(date_str, DATE_FORMAT_INPUT).strftime(DATE_FORMAT_OUTPUT)

if __name__ == '__main__':
    sample_date = "12/31/2020"
    result = convert_date_format(sample_date)
    print(result)