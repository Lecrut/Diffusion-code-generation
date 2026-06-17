def sort_strings(strings):
    return sorted(strings, key=lambda x: x.lower())
if __name__ == '__main__':
    data = ["Apple", "banana", "Cherry", "date"]
    result = sort_strings(data)
    print(result)