def sort_strings_by_length(strings):
    return sorted(strings, key=len)

if __name__ == '__main__':
    sample_input = ["cherry", "date", "fig", "plum", "apricot"]
    result = sort_strings_by_length(sample_input)
    print(result)