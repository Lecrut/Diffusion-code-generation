def sort_strings_by_length(strings):
    length_mapping = {s: len(s) for s in strings}
    return sorted(strings, key=length_mapping.get)

if __name__ == '__main__':
    sample_input = ["blueberry", "raspberry", "strawberry", "blackberry", "a"]
    sorted_output = sort_strings_by_length(sample_input)
    print(sorted_output)