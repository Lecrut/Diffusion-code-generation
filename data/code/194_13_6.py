def longest_item(strings):
    return max(strings, key=len)

if __name__ == '__main__':
    sample_values = ["apple", "banana", "cherry", "date"]
    print(longest_item(sample_values))