def capitalize_words(func):
    """Decorator that capitalizes the first letter of every word in a string."""
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        
        # Handle both strings and return them capitalized
        if isinstance(result, str):
            words = result.split()
            capitalized_words = [word.capitalize() for word in words]
            return ' '.join(capitalized_words)
        
        # If not a string (though the task implies it should be), just pass through or raise error
        else:
            print("Error: Decorator expects to receive a string.")
            return result
        
    return wrapper

@capitalize_words
def greet(name):
    """A function that returns a greeting message."""
    return f"Hello {name}" + "!"

if __name__ == '__main__':
    # Hard-coded sample values for demonstration without user input or files
    test_cases = [
        ("hello world", None),  # Will use the string directly in greet logic if we change it, 
                               # but let's adjust to make sure we actually demonstrate capitalization.
                       ]

# Let's redefine the function slightly to accept a raw sentence for better demonstration capability within this decorator pattern
def process_sentence(sentence):
    """Takes a sentence and returns it."""
    return sentence

@capitalize_words
def enhanced_greet(name, message="!"):
    """Returns a full greeting string like: Hello John !"""
    # In reality, the decorator capitalizes whatever is returned. 
    # Let's construct a raw lowercase sentence to show effect clearly.
    base_sentence = f"hello {name.lower()}" + "!"
    return base_sentence

# Sample execution block running without user input or files
print("Demonstration of capitalized word decorator:")
sample_1 = enhanced_greet("alice")
print(f"Input: 'hello alice!' -> Output: '{sample_1}'")

sample_2 = process_sentence("the quick brown fox jumps over the lazy dog.")
# Note: The original function below does not call the decorator, so let's add a decorated version for sample 2 to be thorough.

@capitalize_words
def raw_text_processor(text):
    return text.lower()

print(f"Input: 'hello world' -> Output via process_sentence (undecorated) would fail logic if called directly like this.")
# Let's just use the decorator on a function that takes input and returns output.
sample_3 = enhanced_greet("bob")
print(f"Sample 2 Input: 'hello bob!' -> Output: '{sample_3}'")

# Final check with raw_text_processor to show direct string manipulation effect if passed as argument? 
# The decorator wraps the return value of a function call.
final_check_result = enhanced_greet("charlie", "wow!") # Adding extra text logic inside wrapper is hard without modifying func body heavily, 
                                                      # so let's stick to simple usage.

print(f"Sample 3 Input: 'hello charlie wow!' (simulated via string construction) -> Output: '{enhanced_greet('dave', '!')}")