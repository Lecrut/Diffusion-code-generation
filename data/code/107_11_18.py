def reformat_date(date_str):
    parts = date_str.split('/')
    return f"{parts[2]}-{parts[0]}-{parts[1]}"

if __name__ == '__main__':
    sample_date = "11/25/2021"
    reformatted_date = reformat_date(sample_date)
    print(reformatted_date)