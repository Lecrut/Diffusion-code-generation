from datetime import datetime

def format_date_string(raw_input: str) -> str:
    date_obj = datetime.strptime(raw_input, "%d-%b-%Y")
    return date_obj.strftime("%Y%m%d")

if __name__ == '__main__':
    input_date = "15-Jul-2022"
    formatted = format_date_string(input_date)
    print(formatted)