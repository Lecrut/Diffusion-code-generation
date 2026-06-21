def longest_item(lst):
    return max(lst, key=str)

if __name__ == '__main__':
    sample = [123, 'hello', 456.789, 'world!', {'a': 1}, [1, 2, 3]]
    print(longest_item(sample))