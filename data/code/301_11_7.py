def convert_dates(date_list):
    return [f"{date[6:]}-{date[0:2]}-{date[3:5]}" for date in date_list]

if __name__ == '__main__':
    sample_dates = ['12/25/2021', '07/04/2022', '11/01/2023']
    print(convert_dates(sample_dates))