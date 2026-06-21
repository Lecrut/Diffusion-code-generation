def process_strings(strings):
    return (s.strip().lower() for s in strings)

if __name__ == '__main__':
    sample_values = ["  Python Programming ", "Data Science", "  Machine Learning  "]
    processed_values = list(process_strings(sample_values))
    print(processed_values)