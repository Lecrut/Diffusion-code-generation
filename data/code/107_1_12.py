from datetime import datetime

def convert_date_format(date_string):
    format_map = {'MM/DD/YYYY': '%m/%d/%Y', 'DD-MM-YYYY': '%d-%m-%Y'}
    source_format = '%m/%d/%Y'
    target_format = '%d-%m-%Y'
    try:
        date_object = datetime.strptime(date_string, format_map[source_format])
        return date_object.strftime(format_map[target_format])
    except ValueError:
        return 'Invalid date format'
if __name__ == '__main__':
    sample_date = '12/31/2023'
    formatted_date = convert_date_format(sample_date)
    print(formatted_date)