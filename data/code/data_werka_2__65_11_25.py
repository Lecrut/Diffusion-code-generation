def print_strings_with_index(strings):
    for index, string in enumerate(strings):
        print(f"Position {index}: {string}")

if __name__ == '__main__':
    sample_data = ["grape", "melon", "kiwi", "orange", "pear"]
    print_strings_with_index(sample_data)