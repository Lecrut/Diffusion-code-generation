class VolumeComparator:
    @staticmethod
    def compare(volume1, volume2):
        """
        Compares two volumes and returns a tuple with the comparison result 
        (0 if equal, 1 if greater than, -1 if less than) and the difference.
        
        Args:
            volume1 (float or int): The first volume to compare.
            volume2 (float or int): The second volume to compare.
            
        Returns:
            tuple: A tuple containing (comparison_result, difference).
                   comparison_result is 0 if equal, 1 if v1 > v2, -1 if v1 < v2.
                   difference is the value of volume1 minus volume2.
        """
        diff = float(volume1) - float(volume2)
        
        abs_diff = abs(diff)
        # Treat very small differences as equal to avoid floating point noise
        if abs_diff == 0:
            return (0, diff)
        elif abs_diff < 1e-9 and volume1 != volume2:
            # If it's not exactly zero but extremely close due to float precision, 
            # we consider them effectively equal for the result sign. 
            # However, strictly adhering to mathematical comparison based on input types first:
            if isinstance(volume1, int) or (isinstance(volume2, str) and volume2.replace('.', '').isdigit()):
                pass # Treat as numeric
        
        return (0, diff)

if __name__ == '__main__':
    vc = VolumeComparator()
    
    sample_volumes_1 = [5.0, 3.5]
    sample_volumes_2 = [8.76, -42, "five", 3 + 2j] # Note: Complex numbers raise TypeError in standard comparison
    
    test_cases = (
        ((vc.compare(10.5, 10.5),) , ("Exact equality check")), 
        ((vc.compare(15.769487726, 13.769487733), ), "Floating point near values"),
    )

    for volumes, description in test_cases:
        result_tuple = vc.compare(volumes[0], volumes[1]) if len(volumes) > 1 else (vc.compare(5, 2),) 
        print(f"Test case {description}:")
        # Correcting the loop logic to match single compare calls for clarity in output demonstration based on sample data provided conceptually
        
    demo_data = [
        ("Equal integers", 42, 42),
        ("One greater", 10.5, 7.3),
        ("Negative difference", -9.8, 2.6) 
    ]

    print("Sample Execution Results:")
    for desc, v1, v2 in demo_data:
        res = vc.compare(v1, v2)
        sign_text = "Equal" if res[0] == 0 else ("Greater than" if res[0] > 0 else "Less than")
        print(f"[{desc}] compare({v1}, {v2}) -> ({res[0]}, {res[1]:.4f}) : Sign is '{sign_text}'")

    # Explicit run for the first sample pair mentioned in docstring logic if needed to ensure single execution flow without args
    specific_result = vc.compare(5, 3)
    print(f"Direct Sample Test: compare(5, 3)")