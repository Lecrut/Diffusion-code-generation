class VolumeComparator:
    def compare(self, volume1, volume2):
        """
        Compares two volumes and returns a tuple containing 
        (comparison_result, difference).
        
        Args:
            volume1 (float or int): First volume value.
            volume2 (float or int): Second volume value.
            
        Returns:
            tuple: A tuple where the first element is -1 if v1 < v2, 0 if equal, 
                   and 1 if v1 > v2. The second element is the absolute difference between them.
        """
        comparison_result = -1 if volume1 < volume2 else (0 if volume1 == volume2 else 1)
        difference = abs(volume1 - volume2)
        return comparison_result, difference

if __name__ == '__main__':
    # Hard-coded sample values to demonstrate functionality without user input or files.
    vol_a = 50.0
    vol_b = 75.5
    
    comparator = VolumeComparator()
    result_tuple = comparator.compare(vol_a, vol_b)
    
    comparison_result, difference = result_tuple
    print(f"Comparison Result: {comparison_result}")
    print(f"Difference: {difference}")