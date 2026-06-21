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
        result.append(dict(zip(headers, values)))
    return result

if __name__ == '__main__':
    sample_csv = """Name,Age,City
Alice,"25,000",New York
Bob,30,"Los Angeles"
Charlie,"40,000",Chicago"""
    parsed_data = parse_csv(sample_csv)
    print(parsed_data)