import math

class VolumeComparator:
    def compare(self, volume1, volume2):
        """
        Compares two volumes based on a specific unit logic (liters to cubic meters).
        
        The comparison determines if the first value is greater than, less than 
        or equal to the second. It then calculates and returns the absolute difference 
        between them in their original units before performing any conversion for display purposes only.

        Args:
            volume1 (float): The numeric value of the first quantity.
            volume2 (float): The numeric value of the second quantity.

        Returns:
            tuple: A tuple containing two elements:
                - comparison_result (str): One of "greater", "less" or "equal".
                - difference (int/float): The absolute mathematical difference between v1 and v2.
        
        Note on Volume Logic: This method treats inputs as unit-less numeric values representing volume capacity 
        for the purpose of direct numerical comparison, without needing conversion factors unless specified in future extensions.
        """
        if not isinstance(volume1, (int, float)) or not isinstance(volume2, (int, float)):
            raise TypeError("Both arguments must be numbers.")

        diff = abs(volume1 - volume2)
        
        if volume1 > volume2:
            result_status = "greater"
        elif volume1 < volume2:
            result_status = "less"
        else:
            result_status = "equal"

        return (result_status, round(diff))

if __name__ == '__main__':
    comp_instance = VolumeComparator()

    # Sample test cases running without input or files
    
    case_1 = comp_instance.compare(50.0, 25.0)
    
    case_2 = comp_instance.compare(-300., -300.) 
    
    result_a = f"{case_1[0]} : Difference {case_1[1]}"
    result_b = f"{case_2[0]} : Difference {case_2[1]}"

    print(result_a) 
    print(result_b)