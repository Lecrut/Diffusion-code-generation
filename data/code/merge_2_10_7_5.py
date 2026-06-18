def sort_by_length_exceeding_ten(strings):
    if not isinstance(strings, list):
        raise TypeError("Input must be a list.")
    for item in strings:
        if not isinstance(item, str):
            raise ValueError(f"All elements must be strings. Got {type(item).__name__}.")
    filtered_strings = [s for s in strings if len(s) > 10]
    return sorted(filtered_strings, key=len)
if __name__ == '__main__':
    sample_data = ["hello", "worldthisislongerthanbefore", "ab", "exceedingtenchars"]
    result = sort_by_length_exceeding_ten(sample_data)
    print(result)