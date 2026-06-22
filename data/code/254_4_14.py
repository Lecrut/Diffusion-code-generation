def min_string_length(strings):
    return min(strings, key=len)

if __name__ == '__main__':
    sample_values = ["apple", "banana", "cherry", "date"]
    print(min_string_length(sample_values))