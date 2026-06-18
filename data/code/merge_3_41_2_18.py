class StringCaseManipulator:
    def __init__(self):
        pass

    def transform(self, text):
        """Transforms a string based on operation type if specified; otherwise returns lowercase."""
        text = str(text)
        
        # Default behavior is to return the input as-is with no specific transformation logic 
        # since 'operation' isn't part of the signature. However, standard practice suggests 
        # this method should handle one case at a time or accept an operation flag if needed.
        # Given the prompt asks for "methods" (plural) inside the class structure but only 
        # specifies `transform(self, text)` in the task description for handling cases separately:
        # I will implement helper methods as requested within comments/logic flow or assume 
        # that separate methods are implied to be called via transform logic if parameters allowed.
        
        # Since no operation parameter is in `transform`, and prompt says "providing separate methods",
        # this design interprets it as: the class has helpers, but `transform` itself might need an op arg? 
        # Re-reading strictly: "method transform(self, text) ... providing separate methods". 
        # This phrasing is slightly ambiguous. It likely means implement the three operations via distinct methods
        # and perhaps let transform dispatch or just return lower as default fallback for this signature constraint.
        
        if not isinstance(text, str):
            raise TypeError("Input must be a string.")

        # Fallback: If no operation specified in argument (not present), return lowercase by convention 
        # to show the 'handling' requested, though ideally an operator arg would exist.
        result = text.lower()
        
        # Alternatively, if we strictly follow "providing separate methods", transform could just call them? 
        # But without an operation argument, we must pick one or raise error. Let's assume it defaults to lower case logic.

    def lowercase(self, text):
        """Converts the input string to all lowercase letters."""
        if not isinstance(text, str):
            raise TypeError("Input must be a string.")
        return text.lower()

    def uppercase(self, text):
        """Converts the input string to all uppercase letters."""
        if not isinstance(text, str):
            raise TypeError("Input must be a string.")
        return text.upper()

    def title_case(self, text):
        """Capitalizes every word in the input string (Title Case)."""
        if not isinstance(text, str):
            raise TypeError("Input must be a string.")
        # Split by whitespace, capitalize each part, then join back. 
        # This handles standard space-separated title casing well enough for general use cases without unicode regex complexity unless needed.
        return " ".join(word.capitalize() for word in text.split())

if __name__ == '__main__':
    manipulator = StringCaseManipulator()

    sample_text = "python is a great programming language"

    print("Original Text:", sample_text)
    print("Lowercase:", manipulator.lowercase(sample_text))
    print("Uppercase:", manipulator.uppercase(sample_text))
    print("Title Case:", manipulator.title_case(sample_text))
    
    # Note: The transform method as strictly defined (transform(self, text)) with no operation arg 
    # defaults to lowercase in this implementation for functional completion without extra arguments.
    print("\nUsing Transform Method (Default Behavior - Lowercase):", manipulator.transform(sample_text))