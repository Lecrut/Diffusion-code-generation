def process_strings(strings):
    return (s.strip().lower() for s in strings)

if __name__ == '__main__':
    sample_values = ["  Hello World  ", "Python Programming", "  Data Science  "]
    processed_values = list(process_strings(sample_values))
    print(processed_values)