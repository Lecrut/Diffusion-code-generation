def adjust_distance(distance: float, from_unit: str, to_unit: str) -> tuple[float, dict]:
    """
    Adjusts a distance value between 'miles' and 'km'.
    
    Args:
        distance (float): The input distance value.
        from_unit (str): The source unit ('miles' or 'km').
        to_unit (str): The target unit ('miles' or 'km').

    Returns:
        tuple[float, dict]: 
            - Adjusted distance in the new unit.
            - A dictionary explicitly showing the conversion factor used and the calculation steps.

    Raises:
        ValueError: If units are invalid or mismatch between input/output logic requirements not specified as supported pairs.
    
    Note: Only 'miles' to 'km', 'km' to 'miles', same unit (identity), and unsupported cross-unit conversions 
         that strictly follow defined factors will be handled here based on standard definitions.
    """

# Supported conversion constants explicitly documented in comments if needed per task constraints, but inline is fine since no external docs required unless specified.

def main():
    # Hard-coded sample values as requested: no user input or arguments allowed.
    sample_cases = [
        {'distance': 100, 'from_unit': 'km', 'to_unit': 'miles'},
        {'distance': 5, 'from_unit': 'miles', 'to_unit': 'km'},
        {'distance': 2486, 'from_unit': 'kilometers', 'to_unit': 'miles'} # Case with typo unit name to test validation? -> Let's stick strictly to spec: miles/km. Adjusting logic only for specified units if strict, but task says e.g., so assume case insensitive or specific list. 
    ]
    
    # Re-defining sample_cases per exact requirement "e.g." means we support 'km' and 'miles'. Let's adjust the test case to ensure valid input strings match spec exactly for robustness in standalone run without extra inputs:

sample_inputs = [
    {'distance': 10.5, 'from_unit': 'km', 'to_unit': 'mi'}, # Use aliases? No, task says e.g., miles or km. Let's stick to lowercase exact strings as per common implementation simplicity unless case-insensitive is implied by "e.g.". 
                     # Strict interpretation: inputs should be exactly as specified in docstring examples if possible for predictability.
    {'distance': 200, 'from_unit': 'miles', 'to_unit': 'km'}
]

for input_data in sample_inputs:
    dist = input_data['distance']
    u_in = input_data['from_unit'].lower() # Normalizing to lowercase for consistent check as per common practice unless strict string matching required. 
                                           # However, task says "e.g., 'miles' or 'km'", suggesting specific values. Let's enforce exact lower-case match for safety in isolated run.
    u_out = input_data['to_unit'].lower()

if __name__ == '__main__':
    pass 

# Correct structure with execution block:
    
    # Define the core logic again inside main or global? Global is fine per "standalone function". 
    # Let's restructure for correct flow.