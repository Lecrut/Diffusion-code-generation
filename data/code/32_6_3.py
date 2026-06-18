def get_phrase_length():
    """Calculates the length of a user-provided phrase."""
    try:
        # Simulating input by using a hardcoded sample value as per constraints
        phrase = "Hello, World!"
        
        # Calculate and print the exact length
        return len(phrase)
    
    except Exception:
        return 0

if __name__ == '__main__':
    result = get_phrase_length()
    print(result)