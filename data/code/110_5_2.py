from datetime import datetime
def date_generator(date_strings):
    parsed_dates = []
    for date_str in date_strings:
        try:
            date_obj = datetime.strptime(date_str, '%Y-%m-%d')
            parsed_dates.append(date_obj)
        except ValueError:
            continue
    parsed_dates.sort()
    for date_obj in parsed_dates:
        yield date_obj
if __name__ == '__main__':
    sample_dates = [
        "2023-10-26",
        "2023-10-25",
        "2023-10-27",
        "2023-10-24",
        "invalid-date"
    ]
    date_gen = date_generator(sample_dates)
    print("Dates yielded by the generator:")
    for date_obj in date_gen:
        print(date_obj.strftime('%Y-%m-%d'))