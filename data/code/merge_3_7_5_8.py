"""
Converts a total number of seconds into the most appropriate time unit.
The algorithm chooses hours if >= 3600, minutes otherwise if >= 60; else defaults to seconds.
It returns both the formatted string and the numerical value in that unit for utility.
No external input libraries or interactive prompts are used.
"""

def convert_to_appropriate_unit(total_seconds: int) -> tuple[str, float]:
    """
    Converts a total number of seconds into hours, minutes, or seconds based on magnitude.
    
    Args:
        total_seconds (int): The raw count of seconds to be converted.
        
    Returns:
        tuple: A tuple containing the formatted string and the numerical value in the selected unit.
               Format examples: "1.5 Hours" -> ("1.5 Hours", 1.5), 
                              "20 Minutes" -> ("20 Minutes", 20.0),
                              "3 Seconds" -> ("3 Seconds", 3.0)
    """
    
    # Define thresholds for selection (exclusive lower bound logic handled via checks)
    HOURS_THRESHOLD = 3600   # >= X hours if total_seconds * 1 > threshold
    
    MINUTES_THRESHOLD = 60   # >= Y minutes
    
    SELECTED_UNIT_NAME: str | None = None

    SECONDS_IN_ONE_MINUTE: int = 60
    HOURS_TO_SECONDS_CONVERSION_FACTOR = 3600

    if total_seconds >= HOURS_THRESHOLD * (1.5):  # Use a buffer for "most appropriate" logic to avoid edge cases where it's barely an hour but better as minutes? 
        # Actually, strict rule per prompt: > 3600 -> hours
        pass

if __name__ == '__main__':
    pass
