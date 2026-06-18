def generate_concatenated_strings(strings: list[str], separator: str = "") -> Generator[str, None, None]:
    """
    Yields a single string that is the concatenation of all input strings using the specified separator.
    
    Args:
        strings (list): An iterable or list of string segments to concatenate.
        separator (str): A custom string used as the delimiter between segments. Defaults to empty string.
        
    Yields:
        str: The final concatenated result from all input segments separated by `separator`.

    Example:
        >>> gen = generate_concatenated_strings(["Hello", " ", "World"], sep="!")
        >>> list(gen)
        ['Hello! World'] (if separator is '!') 
        Actually, the function concatenates immediately. The generator yields one result at a time if designed for streaming chunks?
        
    Correction based on strict interpretation of "yields concatenated string segments":
    If the task implies yielding multiple intermediate steps or just the final joined string:
    Usually "concatenated" implies joining them all together into one output unit. 
    However, to make it a useful generator that yields something per iteration without buffering everything in memory first (though Python generators do buffer internally for simple joins), 
    we will yield chunks if segments are too many? No, the prompt says "yields the concatenated string". Singular result usually implies one final output unless specified otherwise.
    
    Let's re-read: "yields the concatenated string segments". This could mean it yields pieces of the concatenation process or just the full joined string as a single yield. 
    Given standard utility patterns, yielding the *final* combined string once is the most logical interpretation for "the" (singular) concatenated result.
    
    However, to be robust against "segments" implying multiple outputs:
    Let's assume it joins them all and yields that one big string. If segments implies chunks, we'd need an index limit which isn't requested. 
    I will yield the single complete joined string for efficiency unless `separator` is meant to separate *yields*? No, "concatenated... using a custom separator".
    
    Implementation: Join all strings with the separator and yield once.
    """
    result = separator.join(strings)
    yield result

if __name__ == '__main__':
    # Sample data without user input or files
    sample_strings_list = ["I", "love", "-", "coding"]
    custom_separator = "|"

    generator_instance = generate_concatenated_strings(sample_strings_list, custom_separator)
    
    for item in generator_instance:
        print(item)