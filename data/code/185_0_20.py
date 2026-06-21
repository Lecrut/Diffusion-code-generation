def parse_csv(csv_str):
    result = []
    lines = csv_str.strip().split('\n')
    
    def split_line(line):
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
        return values
    
    headers = split_line(lines[0])
    
    for line in lines[1:]:
        values = split_line(line)
        result.append(dict(zip(headers, values)))
    
    return result

if __name__ == '__main__':
    sample_csv = """name,age,"city of residence"
Alice,30,"New York, NY"
Bob,25,"Los Angeles, CA" """
    print(parse_csv(sample_csv))