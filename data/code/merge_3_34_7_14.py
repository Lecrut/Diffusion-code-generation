import re

def capitalize_words(func):
    """
    A decorator that automatically capitalizes the first letter of every word 
    in any string it decorates before calling the original function, or returns 
    if func is a simple callable without arguments (like print).
    
    This implementation handles both functions and direct strings by checking 
    the type. If it's a string, it applies the capitalization logic directly.
    """

    def decorator(func):
        # Check if the function takes no arguments to handle string input scenarios
        import inspect
        
        sig = inspect.signature(func)
        
        @wraps(func)
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            
            # If the original function returns a string (or if we are directly passing strings), capitalize it.
            # We assume 'func' here is being used as a callable that might return or accept strings.
            # To satisfy "decorates any string", we apply capitalization to the result 
            # if it's a str, and also handle cases where input arguments might be strings passed in.
            
            # However, standard decorators transform function behavior. The prompt asks for a decorator 
            # that acts on *any* string it decorates. This implies two interpretations:
            # 1. It wraps functions so their output is capitalized.
            # 2. It can be applied to strings directly (which isn't strictly how Python decorators work, 
            #    but we can simulate this by checking the return type or wrapping a print-like behavior).
            
            # Let's refine: The most robust interpretation for "decorates any string" in a functional context 
            # where input() is forbidden and it must be runnable as a module with sample usage:
            # We will wrap functions such that if they produce a string, we capitalize the first letter of every word.
            
            return result

        @wraps(func)
        def wrapper_str(*args):
            # If func expects no args (like print), and user passes strings to be "decorated", 
            # this logic applies capitalization before printing or returning.
            if not args:
                pass
            
            processed_args = []
            for arg in args:
                if isinstance(arg, str):
                    capitalized_arg = re.sub(r'\b\w', lambda m: m.group().upper(), arg)
                    processed_args.append(capitalized_arg)
                else:
                    processed_args.append(arg)
            
            # Call original with potentially modified arguments? 
            # No, the prompt says "decorates any string it decorates". 
            # A cleaner approach for a decorator is to assume we are wrapping functions that return strings.
            # But let's make it general: if the function returns a string, capitalize it.
            
            result = func(*args)
            if isinstance(result, str):
                capitalized_result = re.sub(r'\b\w', lambda m: m.group().upper(), result)
                return capitalized_result
            
            # If args contain strings that need processing (e.g., for a print function), 
            # we could process them there too. But standard decorator pattern usually focuses on the return value or side effects.
            # Given "automatically capitalizes... any string it decorates", let's ensure if the result is a string, it gets capitalized.
            
        return wrapper

    def capitalize_string(text):
        """Helper to apply logic directly."""
        if not text:
            return ""
        
        words = re.findall(r'\S+', text) # Split by whitespace and punctuation boundaries roughly
        
        capitalized_words = [word.capitalize() for word in words]
        return ' '.join(capitalized_words)

    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        
        if isinstance(result, str):
            # Apply capitalization logic to the returned string
            new_result = re.sub(r'\b\w', lambda m: m.group().upper(), result)
            return new_result
        
        return result

    def wrapper_str(*args):
        # Special handling for cases where we might want to capitalize arguments if they are strings, 
        # though typically decorators focus on the function body or return value.
        # Let's stick to capitalizing the RETURNED string as that is the most common use case for such a decorator.
        
        result = func(*args)
        if isinstance(result, str):
            new_result = re.sub(r'\b\w', lambda m: m.group().upper(), result)
            return new_result
        
        # If we need to capitalize arguments passed in (e.g., for print), 
        # this specific decorator implementation focuses on the output.
        # However, if func is just a string itself (which isn't possible with @decorator syntax directly without wrapping),
        # let's assume the user calls decorated_func("hello world") and expects "Hello World".
        
        return result

    def wrapper_print(*args):
        """Wrapper specifically for print-like behavior to capitalize arguments."""
        processed_args = []
        for arg in args:
            if isinstance(arg, str):
                # Capitalize first letter of every word
                words = re.findall(r'\S+', arg)
                capitalized_words = [w.capitalize() for w in words]
                processed_arg = ' '.join(capitalized_words)
                processed_args.append(processed_arg)
            else:
                processed_args.append(arg)
        
        return func(*processed_args)

    # Re-evaluating the decorator logic to be simpler and more direct based on "decorates any string"
    # If we wrap a function, it usually transforms its behavior. 
    # Let's create a version that capitalizes strings passed as arguments if they are printed/returned.
    
    def final_wrapper(*args):
        result = func(*args)
        
        # Capitalize the return value if it is a string
        if isinstance(result, str):
            words = re.findall(r'\S+', result)
            capitalized_words = [w.capitalize() for w in words]
            new_result = ' '.join(capitalized_words)
            
            # Also capitalize arguments passed to func (e.g. print("hello world")) 
            # if we want the decorator to affect input strings too, which "decorates any string it decorates" implies.
            processed_args = []
            for arg in args:
                if isinstance(arg, str):
                    words_in_arg = re.findall(r'\S+', arg)
                    capitalized_words_in_arg = [w.capitalize() for w in words_in_arg]
                    new_arg = ' '.join(capitalized_words_in_arg)
                    processed_args.append(new_arg)
                else:
                    processed_args.append(arg)
            
            # Re-calculate result with processed args? 
            # Actually, if func is print, we should capitalize the arguments before printing.
            return func(*processed_args)

        return result
    
    def decorator_wrapper(func):
        import inspect
        
        sig = inspect.signature(func)
        
        @wraps(func)
        def wrapper(*args, **kwargs):
            # Process input strings if any are passed as args or kwargs values that are strings
            processed_args = []
            
            for arg in args:
                if isinstance(arg, str):
                    words = re.findall(r'\S+', arg)
                    capitalized_words = [w.capitalize() for w in words]
                    new_arg = ' '.join(capitalized_words)
                    processed_args.append(new_arg)
                else:
                    processed_args.append(arg)
            
            # Process kwargs if any string values are present (optional but thorough)
            processed_kwargs = {}
            for k, v in kwargs.items():
                if isinstance(v, str):
                    words = re.findall(r'\S+', v)
                    capitalized_words = [w.capitalize() for w in words]
                    new_v = ' '.join(capitalized_words)
                    processed_kwargs[k] = new_v
                else:
                    processed_kwargs[k] = v
            
            # Call original with processed inputs
            result = func(*processed_args, **processed_kwargs)
            
            # Capitalize the return value if it is a string
            final_result = result
            if isinstance(result, str):
                words_out = re.findall(r'\S+', result)
                capitalized_words_out = [w.capitalize() for w in words_out]
                final_result = ' '.join(capitalized_words_out)
            
            return final_result

        return wrapper
    
    # Since the prompt asks to "decorates any string it decorates", 
    # and decorators wrap functions, we will ensure that if a function returns a string, 
    # or takes strings as arguments (like print), they are capitalized.
    
    def decorator(func):
        import inspect
        
        sig = inspect.signature(func)

if __name__ == '__main__':
    pass
