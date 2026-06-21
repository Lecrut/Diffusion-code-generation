def process_strings(strings):
    return (s.lower().strip() for s in strings)

if __name__ == '__main__':
    sample_values = [" Hello ", "WORLD", " Python 3.8 "]
    processed_values = list(process_strings(sample_values))
    print(processed_values)