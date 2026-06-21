def parse_csv(csv_string):
    result = []
    current_row = {}
    current_key = None
    in_quotes = False
    escape_next = False

    for char in csv_string:
        if escape_next:
            if char == '"' or char == ',':
                current_key += char
            else:
                raise ValueError("Invalid escape sequence")
            escape_next = False
        elif char == '"':
            in_quotes = not in_quotes
        elif char == ',' and not in_quotes:
            result.append(current_row)
            current_row = {}
            current_key = None
        elif char == '\\' and not in_quotes:
            escape_next = True
        else:
            if current_key is None:
                current_key = char.strip()
            else:
                if current_key in current_row:
                    current_row[current_key] += char
                else:
                    current_row[current_key] = char

    if current_key is not None:
        result.append(current_row)

    return result

if __name__ == '__main__':
    csv_data = 'name,age,"city, state",country\nAlice,30,"New York, NY","USA"\nBob,25,"Los Angeles, CA","USA"'
    print(parse_csv(csv_data))