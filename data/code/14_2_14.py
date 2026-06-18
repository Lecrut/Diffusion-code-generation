class VolumeComparator:
    @staticmethod
    def compare(volume1, volume2):
        """
        Compares two volumes and returns a tuple containing 
        the comparison result ('less', 'equal', or 'greater') 
        and their difference.
        
        Args:
            volume1 (float): First numerical value representing a volume.
            volume2 (float): Second numerical value representing a volume.
            
        Returns:
            tuple: A 2-element tuple containing the comparison result string 
                   as an element of type str, and the difference between 
                   volume1 and volume2 as the second element of type float.
        """
        if volume1 < volume2:
            return ("less", volume1 - volume2)
        elif volume1 == volume2:
            return ("equal", 0.0)
        else:
            return ("greater", volume1 - volume2)

if __name__ == '__main__':
    # Hard-coded sample values for testing without user input
    val_a = 50.75
    val_b = 34.5
    
    result, diff = VolumeComparator.compare(val_a, val_b)
    
    print(f"Comparing {val_a} and {val_b}")
    print(f"Comparison Result: {result}")
    print(f"Difference ({val_a} - {val_b}): {diff}")