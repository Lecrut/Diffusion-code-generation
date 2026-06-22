def split_csv_string(input_string):
    if not isinstance(input_string, str):
        return []
    
    parts = input_string.split(',')
    result = []
    for part in parts:
        trimmed = part.strip()
        if trimmed:
            result.append(trimmed)
    return result

if __name__ == '__main__':
    sample_input = "apple, banana , cherry,, date ,  fig "
    result = split_csv_string(sample_input)
    print(result)