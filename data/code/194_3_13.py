if __name__ == '__main__':
    data = ["apple", "banana", "kiwi", "orange"]
    if not all(isinstance(item, str) for item in data):
        raise ValueError("All elements must be strings")
    
    longest_item = max(data, key=len)
    print(longest_item)