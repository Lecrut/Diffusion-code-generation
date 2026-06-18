def read_integers_from_list(values):
    """
    Helper function to process a list of integers.
    Although standard input is prohibited per instructions, this logic 
    demonstrates how one might filter negative numbers using 
    generator expressions or list comprehensions in Python.
    
    Parameters:
        values (list[int]): A list containing integer elements.
        
    Returns:
        Generator expression that yields only the negative integers from the input list.
    """
    # Using a generator expression for memory efficiency and readability
    yield from [num for num in values if num < 0]

if __name__ == '__main__':
    # Hard-coded sample values as per requirements to avoid interactive prompts or file dependencies
    sample_numbers = [1, -5, 3, -2, 8, -9, 0, -4]

    print("Processing the list of integers...")
    
    # Call the helper function and pass a generator expression directly into it 
    # for demonstration purposes, though in practice we could just filter the sample_numbers here.
    negative_nums = read_integers_from_list(sample_numbers)
    
    if __name__ == '__main__':  # This block executes only once when running as a script
    
        print("Negative numbers found:")
        
        # Iterate over and print each negative number extracted by our logic
        for num in read_integers_from_list([x for x in sample_numbers if isinstance(x, int)]):
            print(num)