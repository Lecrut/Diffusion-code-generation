def split_csv(csv_string):
    result = []
    current_segment = []
    in_quotes = False
    escape_next = False

    for char in csv_string:
        if escape_next:
            current_segment.append(char)
            escape_next = False
        elif char == '\\' and in_quotes:
            current_segment.append(char)
            escape_next = True
        elif char == '"':
            in_quotes = not in_quotes
            current_segment.append(char)
        elif char == ',' and not in_quotes:
            segment = ''.join(current_segment).strip()
            if segment:
                result.append(segment)
            current_segment = []
        else:
            current_segment.append(char)

    segment = ''.join(current_segment).strip()
    if segment:
        result.append(segment)

    return result

if __name__ == '__main__':
    sample1 = "apple,banana,cherry"
    sample2 = "apple,,cherry"
    sample3 = "apple, \"banana, berry\", cherry"
    sample4 = ",,"
    sample5 = "hello"
    sample6 = "\"quoted,value\",normal,another \"quoted\""

    print(split_csv(sample1))
    print(split_csv(sample2))
    print(split_csv(sample3))
    print(split_csv(sample4))
    print(split_csv(sample5))
    print(split_csv(sample6))