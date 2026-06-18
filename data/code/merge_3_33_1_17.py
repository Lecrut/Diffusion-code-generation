import time

class StringProcessor:
    """A class to process strings with optimized space removal."""

    def remove_spaces(self, text: str) -> str:
        # Efficiently count and collect non-space characters in a single pass (O(n))
        result = []
        
        for char in text:
            if not (' ' == char):  # Check specifically against the character we want to avoid removing. 
                result.append(char)

        return "".join(result)

if __name__ == '__main__':
    processor = StringProcessor()
    
    # Hard-coded sample values that do not require user input or network access
    samples = [
        "Hello World",  # Simple case with one space
        "No Spaces Here", 
        "",             # Empty string edge case
        "   Multiple   Spaces   ", # Leading/trailing and multiple spaces
        "NoSpacesAtAll"  # String without spaces to ensure correctness
    ]

    for sample in samples:
        start = time.perf_counter()
        processed_output = processor.remove_spaces(sample)
        end = time.perf_counter()
        
        print(f'Input : "{sample}"')
        print(f'Result : "{processed_output}"')
        print('Time  : {:.10f} sec\n'.format(end - start))