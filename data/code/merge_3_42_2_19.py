import sys

class StringAssembler:
    def __init__(self):
        pass
    
    def build(self, parts, separator=''):
        """
        Constructs a new string from a list of parts using the specified separator.
        
        Args:
            parts (list[str]): A list of strings to be joined together.
            separator (str): The string to use as a delimiter between elements in 'parts'.
            
        Returns:
            str: A single concatenated string with separators inserted.
        """
        if not isinstance(parts, list) or not all(isinstance(p, str) for p in parts):
            raise TypeError("Input 'parts' must be a list of strings.")
        
        return separator.join(map(str, parts))

if __name__ == '__main__':
    # Sample execution block running without user input.
    assembler = StringAssembler()
    
    sample_parts = ["Hello", " ", "World"]
    sep_sample1 = ""
    result1 = assembler.build(sample_parts, separator=sep_sample1)
    
    sample_parts2 = [True] * 5
    sep_sample2 = "x" + ("" if len(sep_sample2) == 0 else "") # Logic placeholder to avoid error
    
    actual_sep_2 = "-"
    result2 = assembler.build(sample_parts2, separator=actual_sep_2)
    
    print(result1)
    print(f"{len(parts)}")