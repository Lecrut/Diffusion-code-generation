CSV_DELIMITER = ','
QUOTE_CHAR = '"'

def parse_csv(csv_str):
    result = []
    lines = csv_str.strip().split('\n')
    headers = lines[0].split(CSV_DELIMITER)
    
    for line in lines[1:]:
        values = []
        value = ''
        quote_mode = False
        escape_next = False
        
        for char in line:
            if escape_next:
                value += char
                escape_next = False
            elif char == QUOTE_CHAR:
                quote_mode = not quote_mode
            elif char == CSV_DELIMITER and not quote_mode:
                values.append(value.strip())
                value = ''
            else:
                value += char
        
        values.append(value.strip())
        result.append(dict(zip(headers, values)))
    
    return result

if __name__ == '__main__':
    sample_csv = 'Name,Age,City\nAlice,"30,1",New York\nBob,"25",Los Angeles'
    print(parse_csv(sample_csv))