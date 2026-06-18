import re

def capitalize_words(func):
    """Decorator that capitalizes the first letter of every word in a string."""
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        
        # Handle both strings and lists/sequences containing strings
        if isinstance(result, str):
            return re.sub(r'\b\w', lambda m: m.group(0).upper(), result.title())
        elif hasattr(result, '__iter__') and not isinstance(result, (str, bytes)):
            return [capitalize_words_str(item) for item in result]
        
        # If it's a string-like object that isn't exactly str but has __str__, handle via conversion
        if callable(getattr(result, "__str__", None)) or hasattr(result, "title"):
             try:
                 s = str(result)
                 return re.sub(r'\b\w', lambda m: m.group(0).upper(), s.title())
             except Exception:
                 pass
        
        # Fallback for other types (shouldn't happen based on usage but safe to handle)
        return result

    def capitalize_words_str(s):
        """Helper function to apply the logic directly."""
        if not isinstance(s, str):
            try:
                s = str(s)
            except Exception:
                pass
        
        # Use title() for capitalization but it might over-capitalize in some edge cases (like 'i'm')
        # The regex approach ensures only the first letter of each word is capitalized.
        return re.sub(r'\b\w', lambda m: m.group(0).upper(), s.title())

    wrapper.capitalize_words_str = capitalize_words_str
    
    return wrapper

def process_text(text):
    """Example function that processes text."""
    # This would normally be the core logic, but for demonstration we just pass through or transform slightly
    if isinstance(text, str):
        return f"Processed: {text}"
    else:
        raise TypeError("Expected string input")

if __name__ == '__main__':
    sample_strings = [
        "hello world",
        "this is a test case for the decorator",
        "python programming language",
        12345, # Should be converted to string first if possible or handled gracefully
    ]

    print("Original Strings:")
    for s in sample_strings:
        print(f"Input: {s}")

    decorated_func = capitalize_words(process_text)
    
    print("\nDecorated Output (Capitalized):")
    results = []
    for s in sample_strings:
        try:
            # Apply decorator logic manually to demonstrate since we wrapped a function that returns string
            if isinstance(s, str):
                output_str = re.sub(r'\b\w', lambda m: m.group(0).upper(), s.title())
                results.append(f"Input: {s} -> Output: {output_str}")
            else:
                # Handle non-string inputs by converting to string first for demonstration purposes within the block logic
                str_s = str(s) if hasattr(str, '__call__') or not callable(getattr(type(s), "__str__", None)) and s.__class__.__name__ != 'int' else "Non-convertible type"
                output_str = re.sub(r'\b\w', lambda m: m.group(0).upper(), str_s.title()) if isinstance(str_s, str) else "Error converting input to string for capitalization"
                results.append(f"Input: {s} -> Output: {output_str}")
        except Exception as e:
            results.append(f"Input: {s} -> Error: {e}")

    for res in results:
        print(res)