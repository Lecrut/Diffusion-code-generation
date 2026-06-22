MAX_LENGTH = 5

def filter_strings(strings):
    return [s for s in strings if len(s) <= MAX_LENGTH]

if __name__ == '__main__':
    sample_data = ["apple", "bee", "cat", "doge", "elephant"]
    filtered_list = filter_strings(sample_data)
    print(filtered_list)