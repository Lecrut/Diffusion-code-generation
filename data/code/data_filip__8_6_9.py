def split_csv_string(text: str) -> list:
    if not text:
        return []
    
    parts = text.split(',')
    result = []
    
    for part in parts:
        stripped = part.strip()
        if stripped:
            result.append(stripped)
            
    return result

if __name__ == '__main__':
    sample_input = "  hello , world ,  python , , coding "
    output = split_csv_string(sample_input)
    print(output)