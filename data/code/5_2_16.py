class LengthComparator:
    def compare(self, length_a, length_b):
        """
        Compares two lengths and returns a descriptive string indicating their relationship.
        
        Parameters:
            length_a (int or float): The first length value.
            length_b (int or float): The second length value.
            
        Returns:
            str: A description of the comparison result.
        """
        if length_a < length_b:
            return f"{length_a} is less than {length_b}"
        elif length_a > length_b:
            return f"{length_a} is greater than {length_b}"
        else:
            return f"{length_a} is equal to {length_b}"

if __name__ == '__main__':
    # Sample test cases with hard-coded values
    comparator = LengthComparator()

    result1 = compare(comparator, 5.0, 3)
    print(result1)  

    result2 = compare(comparator, 7, 7)  
    print(result2)   

    result3 = compare(comparator, 2, 8.5) 
    print(result3)