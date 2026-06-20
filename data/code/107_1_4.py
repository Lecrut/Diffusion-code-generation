from datetime import datetime

def convert_date_format(date_string):
    date_object = datetime.strptime(date_string, '%m/%d/%Y')
    return date_object.strftime('%d-%m-%Y')

if __name__ == '__main__':
    sample_dates = {
        'sample1': '12/31/2023',
        'sample2': '01/01/2024',
        'sample3': '08/25/1999'
    }
    
    for key, date_str in sample_dates.items():
        print(f"{key}: {convert_date_format(date_str)}")