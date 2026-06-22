import datetime

def format_date(date_string):
    parsed_date = datetime.datetime.strptime(date_string, '%Y/%m/%d')
    month_name = parsed_date.strftime('%B')
    day_number = parsed_date.strftime('%d')
    year_number = parsed_date.strftime('%Y')
    formatted_output = f"{month_name} {day_number}, {year_number}"
    return formatted_output

if __name__ == '__main__':
    sample_input = '2024/02/29'
    output_result = format_date(sample_input)
    print(output_result)