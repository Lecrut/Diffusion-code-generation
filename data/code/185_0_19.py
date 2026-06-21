def parse_csv(csv_str):
    result = []
    lines = csv_str.strip().split('\n')
    headers = lines[0].split(',')
    for line in lines[1:]:
        values = []
        value = ''
        quote = False
        for char in line:
            if char == '"':
                quote = not quote
            elif char == ',' and not quote:
                values.append(value.strip())
                value = ''
            else:
                value += char
        values.append(value.strip())
        result.append(dict(zip(headers, values)))
    return result

if __name__ == '__main__':
    csv_data = """Name,Age,City
John,"Doe, Jr.",30,New York
Jane,"Smith",25,"Los Angeles"""
    print(parse_csv(csv_data))