import math

def convert_length(length_km):
    """
    Converts a given length in kilometers to both miles and kilometers.
    
    Parameters:
        length_km (float): The input length in kilometers.
        
    Returns:
        tuple: A tuple containing the value in miles (rounded to 2 decimals) 
               and the original value formatted to 2 decimals.
    """
    MILES_PER_KM = 0.621371
    
    # Calculate miles by converting from kilometers first, then rounding to two decimal places
    length_miles = round(length_km * MILES_PER_KM, 2)
    
    # Format the input length itself for output (already in km as per task context of "to both")
    # Note: The prompt implies conversion TO miles and KM. 
    # Since input is assumed to be a specific unit or just "a length", we treat it generally.
    # However, standard practice when asking for MILES AND KM suggests the input might be in one, output two.
    # Let's assume input 'length' represents a magnitude regardless of origin for this simple converter 
    # OR if input is specifically meant to represent kilometers (common default).
    # To be safe and robust based on "prompts user to enter a length", let's treat it as the value in miles->km? 
    # No, usually conversion tasks assume input unit. Let's re-read: "converts it to both miles and kilometers".
    # This implies one input -> two outputs (miles AND km). If I pass 50, is it 50 feet/meters or 50 units of what?
    # Given the ambiguity without a source unit specified in prompt text alone:
    # Interpretation A: Input is arbitrary magnitude. 
    # Interpretation B: Standard textbook problem where input is treated as miles -> convert to KM, and also show original Miles (formatted).
    # Let's stick to interpretation that matches typical simple scripts: User inputs a value, we output it converted from Kilometers? Or maybe the user just says "50" meaning 50 units.
    
    # Revised Strategy for maximum utility based on common sense in such tasks without explicit unit input field:
    # Assume the INPUT represents kilometers (a very standard starting point for 'enter a length' to get miles/km). 
    # Why? Because usually people ask "How many km is X?" or "Convert X". If I give you 5 and say convert it, giving back 
    # 5 miles and 8km makes no sense if input was already KM. It should be: Input (Miles) -> Output (KM).
    # BUT the prompt says output to BOTH Miles AND Kilometers.
    
    # Let's assume the user provides a value in MILES, we convert that SAME magnitude of physical distance 
    # into KILOMETERS, and also display it back as MILES for reference/comparison? 
    # OR perhaps input is generic feet/units -> miles & km conversion chains.
    
    # Safest bet: Treat the integer/floating point number simply as a scalar length in Kilometers (or arbitrary) 
    # that we want to express in BOTH units relative to Earth's measurement standards, but typically inputs for these 
    # specific "miles and kilometers" tasks are Miles -> convert To Km.
    
    # Let's re-read carefully: "converts it to both miles and kilometers".
    # If I have a string "5", outputting 0.31 mi and 5 km implies the input was treated as KM? 
    # Outputting 8.06 mi (if 13km) vs... 
    # Let's assume the user intends to convert an ENTERED VALUE which we will treat as Miles, then show it in Km AND back in Mi 
    # because maybe they want a conversion tool where input is one unit and output covers both?
    
    # Actually, simplest interpretation of "converts it [the entered length] to both miles and kilometers":
    # Assume the input value IS THE LENGTH IN ONE UNIT (likely Miles given we are asked for Mile AND Km). 
    # So Input X = X Miles. Output: 1) The same X formatted as Mi, 2) X converted to Km.
    
    length_km_out = round(length_miles * math.KM_PER_MILE, 2) 
    
    return f"{length_miles:.2f}", f"{length_km_out:.2f}"

if __name__ == '__main__':
    pass
