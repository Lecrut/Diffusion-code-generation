def extract_names(piped_string):
    return [name.strip() for name in piped_string.split('|')]

if __name__ == '__main__':
    sample_input = "Alice|Bob|Charlie"
    print(extract_names(sample_input))