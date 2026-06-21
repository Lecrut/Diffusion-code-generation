def filter_alphabetic(strings):
    return [s for s in strings if s.isalpha()]

if __name__ == '__main__':
    sample_values = ["hello", "world!", "Python3", "code"]
    try:
        filtered_list = filter_alphabetic(sample_values)
        print(filtered_list)
    except Exception as e:
        print(f"An error occurred: {e}")