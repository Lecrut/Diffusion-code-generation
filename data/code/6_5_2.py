def process_string(s):
    return s.replace(' ', '_')

if __name__ == '__main__':
    sample_text = "Hello World from Python"
    result = process_string(sample_text)
    print(result)