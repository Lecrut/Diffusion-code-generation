class LengthComparator:
    def compare(self, length1_str, unit1, length2_str, unit2):
        """
        Compares two length measurements given as strings with their respective units.
        
        Supported units: 'm', 'cm', 'mm'.
        
        Args:
            length1_str (str): Numeric string representing the first length value.
            unit1 (str): Unit of the first measurement ('m', 'cm', or 'mm').
            length2_str (str): Numeric string representing the second length value.
            unit2 (str): Unit of the second measurement ('m', 'cm', or 'mm').
            
        Returns:
            dict: A dictionary containing the comparison result with keys for values, 
                  units, and outcome status.
        """
        valid_units = {'m': 1000, 'cm': 100, 'mm': 1}
        
        if unit1 not in valid_units or unit2 not in valid_units:
            raise ValueError(f"Unsupported units '{unit1}' and '{unit2}'. Supported: m, cm, mm.")
            
        try:
            val1 = float(length1_str)
            val2 = float(length2_str)
        except ValueError as e:
            return {"status": "error", "message": f"Invalid numeric input for length values. {str(e)}"}

        # Convert both to meters (base unit) and compare
        value_in_meters_1 = val1 * valid_units[unit1]
        value_in_meters_2 = val2 * valid_units[unit2]
        
        result_value_1 = f"{val1} {unit1}"
        result_value_2 = f"{val2} {unit2}"

        if value_in_meters_1 > value_in_meters_2:
            comparison_result = "greater than"
        elif value_in_meters_1 < value_in_meters_2:
            comparison_result = "less than"
        else:
            comparison_result = "equal to"

        return {
            "value1": result_value_1,
            "unit1": unit1,
            "value2": result_value_2,
            "unit2": unit2,
            "comparison_result": f"{result_value_1} is {comparison_result} {result_value_2}",
            "meters_equivalent": {f"{val1}{unit1}": value_in_meters_1, f"{val2}{unit2}": value_in_meters_2},
            "status": "success"
        }

if __name__ == '__main__':
    # Hard-coded sample values for testing without user input or external dependencies
    comparator = LengthComparator()

    test_cases = [
        {"length1_str": "5", "unit1": "m", "length2_str": "3", "unit2": "m"},
        {"length1_str": "100", "unit1": "cm", "length2_str": "1.5", "unit2": "m"},
        {"length1_str": "2000", "unit1": "mm", "length2_str": "2", "unit2": "m"},
    ]

    print("Length Comparison Results:\n")
    
    for i, case in enumerate(test_cases, 1):
        result = comparator.compare(
            length1_str=case["length1_str"], 
            unit1=case["unit1"], 
            length2_str=case["length2_str"], 
            unit2=case["unit2"]
        )

        print(f"Test Case {i}:")
        if result.get("status") == "error":
            print(result)
        else:
            print(f"{result['value1']} ({result['unit1']}) vs {result['value2']} ({result['unit2']}) -> {result['comparison_result']}")
            
    # Example of equal values in different units (e.g., 5m = 500cm) to show 'equal' logic clearly if added, 
    # though the current test cases demonstrate inequality and magnitude conversion.