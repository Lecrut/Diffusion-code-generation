def print_list_with_positions(strings):
    for index, string in enumerate(strings, start=1):
        print(f"{index}: {string}")

if __name__ == '__main__':
    sample_values = ["apple", "banana", "cherry"]
    print_list_with_positions(sample_values)