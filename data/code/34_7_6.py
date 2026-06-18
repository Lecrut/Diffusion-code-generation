import re

def capitalize_words(func):
    """Decorator that capitalizes the first letter of every word in a string."""
    def decorator(*args, **kwargs):
        result = func(*args, **kwargs)
        
        # Check if result is a string and contains words to process
        if isinstance(result, str):
            # Split into words using regex (handles multiple spaces correctly)
            words = re.findall(r'\S+', result)
            
            # Capitalize each word and join back with original spacing structure preserved roughly via joining
            capitalized_words = [word.capitalize() for word in words]
            
            # Reconstruct the string. Note: simple approach replaces separators, 
            # but strictly speaking "every word" implies we need to preserve non-word characters if needed.
            # For robustness without complex parsing of original spacing, a standard split/join is often expected unless specified otherwise.
            # However, to be most accurate to the prompt ("automatically capitalizes... every word"), 
            # we will replace spaces with single space after joining for clean output as per common decorator expectations unless specific preservation logic was requested.
            return ' '.join(capitalized_words) if any(words) else result
            
        return result

    return decorator

# Example usage demonstrating functionality
if __name__ == '__main__':
    @capitalize_words
    def greet(name):
        # Assuming the function returns a string containing words to be capitalized by the decorator logic applied here.
        # The prompt asks for a decorator on ANY string it decorates. 
        # Since we are wrapping a function that returns a string, this matches the requirement.
        return f"hello {name} welcome to python programming today."

    sample_names = ["alice", "bob smith"]
    
    print("Output:", greet(sample_names[0]))