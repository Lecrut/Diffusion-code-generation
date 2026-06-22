def find_min_length_string(strings):
    min_length = float('inf')
    min_string = None
    for string in strings:
        current_length = len(string)
        if current_length < min_length:
            min_length = current_length
            min_string = string
    return min_string

if __name__ == '__main__':
    sample_values = ["python", "java", "c", "ruby"]
    print(find_min_length_string(sample_values))