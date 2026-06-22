def min_by_length(strings):
    return min(strings, key=len)

if __name__ == '__main__':
    sample_strings = ["apple", "banana", "cherry", "date"]
    print(min_by_length(sample_strings))