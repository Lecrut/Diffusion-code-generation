def process_string(s):
    parts = s.split(',')
    normalized = [part.strip().lower() for part in parts]
    unique_parts = list(dict.fromkeys(normalized))
    return unique_parts

if __name__ == '__main__':
    sample = "Apple, banana, APPLE, banana, cherry"
    result = process_string(sample)
    print(result)