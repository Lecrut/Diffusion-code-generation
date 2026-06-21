def sort_strings_by_length(strings):
    if not strings:
        return []
    return sorted(strings, key=len)

if __name__ == '__main__':
    sample_values = ["blueberry", "raspberry", "strawberry", "blackberry", "a"]
    sorted_values = sort_strings_by_length(sample_values)
    print(sorted_values)