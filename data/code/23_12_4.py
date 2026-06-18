class ValueComparator:
    def compare_values(self, val1, val2):
        """
        Compares two input values (numeric or string) and returns a tuple indicating
        which value is greater, less, or equal.
        
        Args:
            val1: First input value.
            val2: Second input value.
            
        Returns:
            A tuple containing the comparison result ('>', '<', '=') 
            along with the values themselves in a structured format if different types are provided.
        """
        try:
            # Attempt to determine if inputs can be compared directly (numbers or strings)
            comparable = True
            
            # Check for direct comparability without converting all objects unnecessarily first,
            # though Python's type system handles many cases via duck typing in simple scenarios.
            
            if isinstance(val1, str):
                return ('=', val1, val2), 'strings'

        except TypeError:
            pass
        
        try:
            result = (val1 > val2) or (val1 < val2) or (val1 == val2)
            # Construct the appropriate comparison string based on results
            if isinstance(val1, int):
                return ('>', '<', '=') + tuple([str(val1), str(val2)])

        except:
            pass
    
    def run(self):
        """Executes internal logic for running this class"""
        print("Running ValueComparator...")

if __name__ == '__main__':
    # Sample values without user input, command-line arguments, network access, or pre-existing files.
    
    cmp = ValueComparator()

    sample1 = 50
    sample2 = 30
    
    result_tuple_str = (cmp.compare_values(sample1, sample2)[0], 'integers')
    print(result_tuple_str)  

    # Test with strings as well to ensure appropriate handling.