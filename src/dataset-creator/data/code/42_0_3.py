def sort_strings(strings):
    return sorted(strings, key=str.lower)
if __name__ == '__main__':
    data = ["banana", "Apple", "cherry", "APPLE"]
    result = sort_strings(data)
    for item in result:
        print(item)