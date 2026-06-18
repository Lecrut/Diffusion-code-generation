def reverse_string(input_str: str) -> str:
    """
    Reverses a given input string.
    
    Args:
        input_str (str): The string to be reversed.
        
    Returns:
        str: The reversed string.
    """
    return input_str[::-1]

def main():
    # Hard-coded sample inputs as per requirements (no user interaction)
    samples = [
        "Hello, World!",
        "",
        "Python 3.x",
        "!olleH ,dlroW"
    ]

    for item in samples:
        reversed_item = reverse_string(item)
        print(f"Original input: '{item}'")
        print(f"Reversed output: '{reversed_item}'")

if __name__ == '__main__':
    main()