def parse_csv(csv_str):
    result = []
    lines = csv_str.strip().split('\n')
    headers = lines[0].split(',')
    for line in lines[1:]:
        values = []
        value = ''
        quote_mode = False
        escape_next = False
        for char in line:
            if escape_next:
                value += char
                escape_next = False
            elif char == '\\':
                escape_next = True
            elif char == '"':
                quote_mode = not quote_mode
            elif char == ',' and not quote_mode:
                values.append(value.strip())
                value = ''
            else:
                value += char
        values.append(value.strip())
        if len(values) != len(headers):
            raise ValueError("Row does not match header length")
        result.append(dict(zip(headers, values)))

if __name__ == '__main__':
    csv_data = """name,age,city
Alice,30,"New York"
Bob,25,"Los Angeles"""
    try:
        parsed_data = parse_csv(csv_data)
        print(parsed_data)
    except ValueError as e:
        print(e)