from datetime import datetime

def sort_dates(date_strings):
    parsed_dates = []
    for date_str in date_strings:
        dt = datetime.strptime(date_str, '%d/%m/%Y')
        parsed_dates.append((dt, date_str))
    parsed_dates.sort(key=lambda x: x[0])
    return [item[1] for item in parsed_dates]

if __name__ == '__main__':
    sample_dates = ['25/12/2023', '01/01/2024', '15/06/2023', '31/12/2022']
    sorted_dates = sort_dates(sample_dates)
    print(sorted_dates)