import sys

def reverse_string(s: str) -> str:
    """Reverses the order of characters in a given string."""
    return s[::-1]

if __name__ == '__main__':
    # Sample input hard-coded to ensure no user interaction or external dependencies
    sample = "Hello, World!"
    
    reversed_result = reverse_string(sample)
    
    print(f"Original: {sample}")
    print(f"Reversed:{reversed_result}")