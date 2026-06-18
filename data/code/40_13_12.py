def get_first_letter(s: str) -> str:
    """Returns the first letter of the string if it exists, otherwise an empty string."""
    return s[0] if len(s) > 0 else ""

if __name__ == '__main__':
    # Sample test cases without any user input or external dependencies
    samples = [
        "Hello World",
        "",
        "a",
        "!@#",
        None,  # Will be handled gracefully by returning empty string due to type check logic below if needed, 
              # but per spec we only take a single string. If input is not str in real use, handle it here:
    ]

    # Adjusting samples to ensure they are all strings as the function expects str