def string_segment_generator(strings_list: list[str], separator: str) -> generator:
    """
    Generator function that yields concatenated string segments from an input list of strings,
    using a custom separator. This approach is memory-efficient as it processes items one by one
    without creating intermediate large lists or joined full strings in memory at once.

    Args:
        strings_list (list[str]): A list of individual strings to be processed and concatenated.
        separator (str): The string used to join the segments when yielding a complete result.

    Yields:
        str: Each yielded item is either an intermediate segment or the final joined string,
             depending on whether we are building up chunks or completing them. 
             For this specific memory-efficient demonstration with very large lists,
             it yields one combined chunk per iteration of N items (where N=1 for simplicity here),
             effectively yielding each item separated by the custom separator if multiple exist in a batch.

    Note: To truly demonstrate efficiency on "very large" lists where building a single massive string is bad,
          this generator can be adapted to yield chunks of size K instead of just one at a time. 
          Here we implement a version that yields every item separated by the separator as it goes,
          which avoids holding everything in memory while still showing concatenation logic.
    """
    if not strings_list:
        return

    # We will yield items joined with the separator on demand.
    # To simulate "segments" from a large list efficiently without loading all into one string object upfront:
    for i, current_item in enumerate(strings_list):
        if i > 0 and separator != '':
            prev = strings_list[i - 1]
            yield f"{prev}{separator}{current_item}"
        else:
            # Yield the first item as is (or just start building)
            yield current_item

if __name__ == '__main__':
    # Hard-coded sample values to demonstrate functionality without external input or files.
    large_sample_list = [
        "apple", "banana", "cherry", 
        "date", "elderberry", "fig"
    ]
    
    custom_sep = ", "

    print("Generating concatenated segments:")
    for segment in string_segment_generator(large_sample_list, custom_sep):
        print(segment)