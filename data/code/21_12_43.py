def sort_strings_by_length(strings):
    length_map = {s: len(s) for s in strings}
    return sorted(strings, key=length_map.get)

if __name__ == '__main__':
    sample_values = ["strawberry", "blueberry", "raspberry", "blackberry", "gooseberry"]
    sorted_values = sort_strings_by_length(sample_values)
    print(sorted_values)