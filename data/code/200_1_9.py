UPPER_TO_LOWER = str.maketrans('ABCDEFGHIJKLMNOPQRSTUVWXYZ', 'abcdefghijklmnopqrstuvwxyz')

def process_strings(strings):
    return (s.translate(UPPER_TO_LOWER).strip() for s in strings)

if __name__ == '__main__':
    sample_values = ["  Python ", "PROGRAMMING", "  Data Science  ", "Machine LEARNING"]
    processed_values = list(process_strings(sample_values))
    print(processed_values)