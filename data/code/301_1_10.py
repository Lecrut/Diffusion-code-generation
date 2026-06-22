def convert_dates(date_list):
    return [f"{date.split('/')[2]}-{date.split('/')[0]}-{date.split('/')[1]}" for date in date_list]

if __name__ == '__main__':
    sample_dates = ['12/31/2020', '01/01/2021', '11/15/2022']
    print(convert_dates(sample_dates))