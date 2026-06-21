if __name__ == '__main__':
    data = ["apple", "banana", "kiwi", "orange"]
    if isinstance(data, list) and all(isinstance(item, str) for item in data):
        longest_item = max(data, key=len)
        print(longest_item)
    else:
        raise ValueError("Input must be a list of strings")