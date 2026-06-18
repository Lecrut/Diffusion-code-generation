def case_swap(text: str) -> dict[str, str]:
    """
    Returns a dictionary mapping 'lower', 'upper', and 'title' 
    to their respective case transformations of the input string.
    
    Args:
        text (str): The input string to transform.
        
    Returns:
        dict[str, str]: A dictionary with keys 'lower', 'upper', and 'title'.
    """
    lower_text = text.lower()
    upper_text = text.upper()
    title_text = ''.join(word.capitalize() for word in text.split())
    
    return {
        'lower': lower_text,
        'upper': upper_text,
        'title': title_text
    }

if __name__ == '__main__':
    sample_input = "Hello World"
    result = case_swap(sample_input)
    print(f"Input: '{sample_input}'")
    print("Transformations:")
    for key in ['lower', 'upper', 'title']:
        print(f"{key}: {result[key]}")