def build_string_with_spacing(elements):
    """
    Iteratively builds a string by appending each element from an input list,
    managing necessary spacing between elements correctly.
    
    If the list is empty, returns an empty string.
    Otherwise, joins all elements with a single space in between them.
    
    Args:
        elements (list): A list of strings or other objects that can be converted to strings.
        
    Returns:
        str: The resulting joined string with spaces separating the original items.
    """
    if not elements:
        return ""
    
    result = []
    for i, element in enumerate(elements):
        # Convert each element to a string representation
        item_str = str(element)
        
        # Append space before current item unless it's the first one (index 0)
        if i > 0:
            result.append(" ")
            
        result.append(item_str)
    
    return "".join(result)

if __name__ == '__main__':
    # Hard-coded sample values as per requirements
    sample_list = ["Hello", "World", "This", "Is", "A", "Test"]
    
    output_string = build_string_with_spacing(sample_list)
    
    print(output_string)

# Additional test case with empty list and mixed types (though input() is not used here)
if False:  # Keeping this block commented out or inactive to ensure no side effects if run directly in some environments, 
           # but since the task says "runnable", we can actually include a second simple check inside main logic without extra prompts.
    empty_list = []
    print(build_string_with_spacing(empty_list))

# Another quick verification with single element
single_item = ["Only"]
print(build_string_with_spacing(single_item))