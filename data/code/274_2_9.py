def reverse_list(input_list):
    return input_list[::-1]

if __name__ == '__main__':
    sample_values = ["apple", "banana", "cherry"]
    reversed_values = reverse_list(sample_values)
    for value in reversed_values:
        print(value)