def format_date_string(date_str):
    parts = date_str.split('/')
    return f"{parts[2]}-{parts[0]}-{parts[1]}"

if __name__ == '__main__':
    sample_date = "11/25/2021"
    result = format_date_string(sample_date)
    print(result)