def total_string_length(strings):
    """
    Calculates the total combined length of all strings in a list.

    Args:
        strings (list[str]): A list containing string elements.

    Returns:
        int: The sum of lengths of all strings.

    Performance Note:
        This function uses a generator expression passed to built-in 'sum()', 
        which is implemented efficiently in CPython and avoids creating an intermediate list,
        making it memory efficient for large inputs while remaining readable.
    """
    return sum(len(s) for s in strings if isinstance(s, str))

if __name__ == '__main__':
    # Hard-coded sample values as per requirements (no user input or external files needed)
    sample_data = ["Hello", "World", "", "Python", "is"]
    
    result = total_string_length(sample_data)
    
    print(f"Total combined length: {result}")