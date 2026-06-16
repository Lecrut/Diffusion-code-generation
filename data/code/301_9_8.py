import datetime
def convert_date_format(date_str: str, from_format: str, to_format: str) -> str:
    try:
        if from_format == 'YYYY/MM/DD' and to_format == 'MM/DD/YYYY':
            dt_obj = datetime.datetime.strptime(date_str, '%Y/%m/%d')
            return dt_obj.strftime('%m/%d/%Y')
        elif from_format == 'MM/DD/YYYY' and to_format == 'YYYY/MM/DD':
            dt_obj = datetime.datetime.strptime(date_str, '%m/%d/%Y')
            return dt_obj.strftime('%Y/%m/%d')
        else:
            raise ValueError("Unsupported format conversion requested.")
    except ValueError as e:
        raise ValueError(f"Error parsing date string '{date_str}' with specified formats: {e}")
if __name__ == '__main__':
    sample1 = "2023/10/27"
    print(f"Original: {sample1}, Format YYYY/MM/DD -> MM/DD/YYYY: {convert_date_format(sample1, 'YYYY/MM/DD', 'MM/DD/YYYY')}")
    sample2 = "11/15/2024"
    print(f"Original: {sample2}, Format MM/DD/YYYY -> YYYY/MM/DD: {convert_date_format(sample2, 'MM/DD/YYYY', 'YYYY/MM/DD')}")
    sample3 = "2025/01/01"
    print(f"Original: {sample3}, Format YYYY/MM/DD -> MM/DD/YYYY: {convert_date_format(sample3, 'YYYY/MM/DD', 'MM/DD/YYYY')}")
    try:
        convert_date_format("2024-12-31", 'YYYY/MM/DD', 'MM/DD/YYYY')
    except ValueError as e:
        print(f"Error caught for invalid input: {e}")