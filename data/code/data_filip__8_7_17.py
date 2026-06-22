def parse_comma_separated(input_string):
    if not input_string:
        return []
    
    parts = input_string.split(',')
    result = []
    
    for part in parts:
        stripped = part.strip()
        if stripped:
            result.append(stripped)
            
    return result

if __name__ == '__main__':
    sample_input = "apple, banana,, cherry , ,date"
    output = parse_comma_separated(sample_input)
    print(output)