def sort_by_length_exceeding_ten(items):
    if not isinstance(items, list):
        raise TypeError("Input must be a list.")
    for item in items:
        if not isinstance(item, str):
            raise ValueError(f"All elements must be strings. Got {type(item).__name__}.")
    filtered_items = [item for item in items if len(item) > 10]
    try:
        sorted_filtered = sorted(filtered_items, key=len)
        return {"original": items, "filtered_sorted": sorted_filtered}
    except Exception as e:
        raise RuntimeError(f"An unexpected error occurred during sorting.") from e
if __name__ == '__main__':
    sample_data = ["short", "this_is_a_long_string_test", "medium_length", "another_very_long_text_example"]
    result = sort_by_length_exceeding_ten(sample_data)
    print(result["filtered_sorted"])