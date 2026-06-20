def is_weekday(date_str):
    return date_str.split('-')[2] not in ('06', '07')
if __name__ == '__main__':
    print(is_weekday('2023-10-05'))
    print(is_weekday('2023-10-06'))