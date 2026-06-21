def sort_alphabetically(strings):
    return sorted(strings, key=lambda s: s.lower())

if __name__ == '__main__':
    sample_values = ["Banana", "apple", "Cherry", "date"]
    result = sort_alphabetically(sample_values)
    print(result)