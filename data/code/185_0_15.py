def parse_csv(csv_str):
    result = []
    current_row = {}
    current_key = None
    in_quotes = False
    escape_next = False

    for char in csv_str:
        if escape_next:
            current_key += char
            escape_next = False
        elif char == '\\':
            escape_next = True
        elif char == '"':
            in_quotes = not in_quotes
        elif char == ',' and not in_quotes:
            result.append(current_row)
            current_row = {}
            current_key = None
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
    sample_csv = 'name,age,"city, state",email\nAlice,30,"New York, NY","alice@example.com"\nBob,25,"Los Angeles, CA","bob@example.com"'
    print(parse_csv(sample_csv))