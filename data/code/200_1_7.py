def process_strings(strings):
    if not all(isinstance(s, str) for s in strings):
        raise ValueError("All elements must be strings")
    return (s.strip().lower() for s in strings)

if __name__ == '__main__':
    sample_values = ["  Python ", "PROGRAMMING", "  Data Science  ", "Machine LEARNING"]
    processed_values = list(process_strings(sample_values))
    print(processed_values)