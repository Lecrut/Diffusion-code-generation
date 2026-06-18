def sort_strings(strings):
    return sorted(strings, key=str.lower)
if __name__ == '__main__':
    data = ["banana", "Apple", "cherry", "DATE"]
    result = sort_strings(data)
    print("\n".join(result))