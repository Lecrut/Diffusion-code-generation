def validate_strings(data):
    if not all(isinstance(x, str) for x in data):
        raise ValueError("All elements must be strings")

def process_strings(strings):
    validate_strings(strings)
    return (s.strip().lower() for s in strings)

if __name__ == '__main__':
    sample_values = ["  Hello World  ", "Python Programming", "  Data Science  "]
    processed_values = list(process_strings(sample_values))
    print(processed_values)