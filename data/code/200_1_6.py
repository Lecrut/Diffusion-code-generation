SAMPLE_STRINGS = ['  Python ', 'PROGRAMMING', '  Data Science  ', 'Machine LEARNING']

def process_strings(strings):
    return (s.strip().lower() for s in strings)
if __name__ == '__main__':
    processed_values = list(process_strings(SAMPLE_STRINGS))
    print(processed_values)