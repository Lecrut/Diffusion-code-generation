def process_csv_string(data: str) -> list:
    parts = data.split(",")
    return [p for p in parts if p != ""]

if __name__ == '__main__':
    csv_data = "a,,b,c,,d"
    result = process_csv_string(csv_data)
    print(result)