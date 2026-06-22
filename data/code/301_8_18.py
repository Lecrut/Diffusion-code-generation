from datetime import datetime

def convert_date_format(date_str, input_format='%m/%d/%Y', output_format='%d/%m/%Y'):
    date_obj = datetime.strptime(date_str, input_format)
    return date_obj.strftime(output_format)

if __name__ == '__main__':
    sample_dates = ['10/27/2023', '01/05/2024']
    for date in sample_dates:
        converted_date = convert_date_format(date)
        print(f"Original Date: {date}, Converted Date: {converted_date}")