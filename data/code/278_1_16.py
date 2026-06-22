def print_separately(strings):
    if not all(isinstance(item, str) for item in strings):
        raise ValueError("All elements in the list must be strings")
    for index, string in enumerate(strings, start=1):
        print(f"{index}. {string}")

if __name__ == '__main__':
    data1 = ["apple", "banana", "cherry"]
    print_separately(data1)
    data2 = ["dog", "cat", "mouse"]
    print_separately(data2)