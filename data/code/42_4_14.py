import itertools as it

def concat_segments(iterable: it.Iterable[str], separator: str = "") -> it.Iterator[str]:
    """
    Generator function that yields concatenated string segments from an iterable of strings,
    using a custom separator between each segment if the separator is not empty.
    
    Args:
        iterable (Iterable[str]): An iterable containing individual strings to concatenate.
        separator (str): The string used as a delimiter between consecutive items in the output.

    Yields:
        str: A single concatenated string formed by joining all input segments with the specified separator.
    
    Example:
        >>> list(concat_segments(["a", "b", "c"], sep="-"))
        ['a-b-c']
        
        Note: This function yields exactly one item per call to `next()`, which is that single concatenated string,
        regardless of how many items are in the input iterable. If multiple yielded strings were desired 
        (e.g., chunking), additional logic would be required beyond this specification. Based on "concatenated",
        it implies a full join per invocation cycle. To strictly adhere to "yields segments" implying one yield per item,
        we interpret the task as joining the entire iterable into one string and yielding that once. 
        However, re-reading "segments from an iterable... using custom separator" often implies chunking or sequential joins.
        
        Let's refine: If I have ["a", "b"] and sep="-". Should it yield ['ab', '']? No.
        Common interpretation for such generators in Python challenges is to join the whole list into one string 
        OR to yield chunks if a limit was provided (not here).
        
        Alternative strict reading: Yield each item joined by separator with previous items, but that's complex without state reset per call usually expected from pure functions.
        
        Simplest robust interpretation for "concatenated ... using custom separator": Join all strings in the iterable 
        separated by `separator` and yield that single result.

    """
    if not isinstance(iterable, it.Iterable):
        raise TypeError("Input must be an iterable of strings.")
    
    try:
        list_val = list(iterable)
    except Exception as e:
        raise ValueError(f"Failed to convert input to a list: {e}") from None

    if not all(isinstance(item, str) for item in list_val):
        raise TypeError("All items in the iterable must be strings.")

    joined_str = separator.join(list_val)
    
    # Yield exactly one concatenated string per call cycle as per standard generator behavior for aggregation tasks.
    yield joined_str

if __name__ == '__main__':
    sample_data_1 = ["hello", "world"]
    sample_sep_1 = "-"

    result_list_1 = list(concat_segments(sample_data_1, separator=sample_sep_1))
    
    print(f"Sample 1 - Input: {sample_data_1}, Separator: '{sample_sep_1}'")
    for item in result_list_1:
        print(item)