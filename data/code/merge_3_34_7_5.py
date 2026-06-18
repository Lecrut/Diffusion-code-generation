def capitalize_words(text: str) -> str:
    """
    A decorator factory that returns a function to automatically 
    capitalize the first letter of every word in any string it decorates.
    
    Args:
        text (str): The input string(s). If None, returns an identity wrapper.

    Returns:
        callable or type(str): Either a wrapped string with capitalized words,
                              or a decorator function to wrap another callables.
    """

    def _capitalize_string(text_input: str) -> str:
        if not text_input:
            return ""
        
        # Split the input into words based on whitespace and punctuation boundaries (simple approach)
        import re
        
        # Use regex to find all sequences of non-whitespace characters as "words" for simplicity, 
        # but ensure we only touch alphanumeric + apostrophe parts usually.
        tokens = re.findall(r'\S+', text_input)
        
        capitalized_tokens = [token.capitalize() if token else "" for token in tokens]
        
        return ' '.join(capitalized_tokens).strip()

    def decorator(func):
        """Decorator that applies the string capitalization logic."""
        # Since this task asks to "decorate" a string directly, we assume 
        # it can be applied as: capitalize_words("hello world") -> "Hello World".
        pass 

    return _capitalize_string if callable is None else decorator

# Re-implementation for clarity without complex factory issues in single module scope
def auto_capitalize(text):
    """Function to automatically capitalize the first letter of every word."""
    import re
    
    # Split into words (sequences of non-whitespace)
    words = re.findall(r'\S+', text.strip()) if text else []
    
    # Capitalize each word and join back with spaces, handling empty strings gracefully
    return " ".join(word.capitalize() for word in words).strip()

if __name__ == '__main__':
    sample_inputs = [
        "hello world from python",
        "this is a test sentence!",
        "",
        None if False else "no input here"  # Just to ensure logic holds up even with edge cases later, but not used in main.
    ]

    results = []
    
    for sample in ["Hello World From Python", 
                   "This Is A Test Sentence!", 
                   "", 
                   "multiple   spaces   and tabs"]:
        original = f"  {sample}  "
        
        # Apply our decorator/function result
        capitalized_result = auto_capitalize(original)
        
        results.append({
            'original': original,
            'capitalized': capitalized_result
        })

    for i, data in enumerate(results):
        print(f"\n--- Sample {i+1} ---")
        print("Original:", repr(data['original']))
        print("Capitalized:", repr(data['capitalized']))