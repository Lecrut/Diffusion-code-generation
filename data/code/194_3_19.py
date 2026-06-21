MAX_LENGTH_KEY = len

if __name__ == '__main__':
    sample_data = ["apple", "banana", "kiwi", "orange"]
    longest_item = max(sample_data, key=MAX_LENGTH_KEY)
    print(longest_item)