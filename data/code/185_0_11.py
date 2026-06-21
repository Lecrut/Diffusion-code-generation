def parse_csv(csv_str):
    result = []
    current_row = {}
    current_key = None
    in_quotes = False
    escape_next = False

    for char in csv_str:
        if escape_next:
            if char == '"' or char == ',':
                current_value += char
            else:
                current_value += '\\' + char
            escape_next = False
        elif char == '"':
            in_quotes = not in_quotes
        elif char == ',' and not in_quotes:
            if current_key is not None:
                current_row[current_key] = current_value.strip()
                current_value = ''
                current_key = None
        else:
            if current_key is None:
                current_key = char.strip()
            else:
                current_value += char

    if current_key is not None:
        current_row[current_key] = current_value.strip()

    result.append(current_row)
    return result

if __name__ == '__main__':
    csv_data = 'name,age\n"John Doe",30\nJane,"Doe, Jr."'
    print(parse_csv(csv_data))