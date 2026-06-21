def parse_csv(csv_str):
    result = []
    lines = csv_str.strip().split('\n')
    headers = lines[0].split(',')
    for line in lines[1:]:
        values = []
        value = ''
        quote_mode = False
        for char in line:
            if char == '"':
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
    csv_data = """name,age,city
Alice,"25,000",New York
Bob,30,"Los Angeles"""
    print(parse_csv(csv_data))