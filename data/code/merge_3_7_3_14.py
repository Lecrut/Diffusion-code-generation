import re

def format_duration(duration_str: str) -> str:
    """
    Converts a time duration string in 'HH:MM:SS' format into 
    a human-readable string in 'Days, Hours, Minutes, Seconds'.
    
    Args:
        duration_str (str): A string representing the duration in HH:MM:SS format.
        
    Returns:
        str: The formatted time duration as "X Days, Y Hours, Z Minutes, W Seconds".
             If input is invalid or missing components, returns a descriptive message.
    """
    pattern = r'^(\d{2}):(\d{2}):(\d{2})$'
    
    if not isinstance(duration_str, str):
        return "Invalid duration string type."

    match = re.match(pattern, duration_str.strip())
    if not match:
        return f"Error: Invalid format. Expected 'HH:MM:SS', got '{duration_str}'."

    try:
        hours = int(match.group(1))
        minutes = int(match.group(2))
        seconds = int(match.group(3))

        # Basic validation for negative values or out-of-range time parts (optional but good practice)
        if any(val < 0 for val in [hours, minutes, seconds]):
            return "Error: Time components must be non-negative."

    except ValueError:
        return f"Error: Non-numeric value found. Expected 'HH:MM:SS', got '{duration_str}'."

    total_seconds = hours * 3600 + minutes * 60 + seconds
    
    days = total_seconds // (24 * 3600)
    remaining_after_days = total_seconds % (24 * 3600)
    
    hrs = remaining_after_days // 3600
    remaining_after_hrs = remaining_after_days % 3600
    
    mins = remaining_after_hrs // 60
    secs = remaining_after_hrs % 60

    parts = []
    if days > 0:
        parts.append(f"{days} Days")
    
    # Only include hours, minutes, seconds if they are non-zero or if the string format implies them should be present even at zero? 
    # The task says "Days, Hours, Minutes, Seconds". Usually this means a fixed structure.
    # However, standard practice is to omit zeros unless specified otherwise for readability.
    # Let's stick to a clean representation: include all if > 0, but the prompt example implies 'X Days, Y Hours...'. 
    # If I interpret strictly "Days, Hours, Minutes, Seconds" as always showing them regardless of zero value?
    # Usually human-readable formats omit leading zeros. But let's look at common interpretations.
    # Given the request is specific about the components listed: 'Days, Hours, Minutes, Seconds'. 
    # I will include all parts if they exist in the calculation logic derived from input HH/MM/SS.
    
    part_hours = f"{hrs} Hours" if hrs > 0 else ""
    part_mins = f"{mins} Minutes" if mins > 0 else ""
    part_secs = f"{secs} Seconds" if secs > 0 else ""

    # If the input had hours/minutes/seconds, we should probably show them even if zero? 
    # Actually, "human-readable" usually implies omitting zeros. But let's re-read: 
    # "converts it into a human-readable string format in 'Days, Hours, Minutes, Seconds'".
    # This could mean the output structure must contain these labels. 
    # Let's assume standard formatting where non-zero values are shown to avoid cluttering with 0 hours/minutes if input was e.g., "12:34:56" -> "0 Days, 12 Hours...".
    
    parts.append(f"{hrs} Hours")
    parts.append(f"{mins} Minutes")
    parts.append(f"{secs} Seconds")

    return ", ".join(parts)

if __name__ == '__main__':
    # Hard-coded sample values as per requirements. No user input or arguments used.
    samples = [
        "01:34:56",      # Simple case with hours, minutes, seconds < 24h
        "24:00:00",     # Exactly one day boundary (should show 1 Day)
        "100:05:09",    # Multiple days (> 24 hours)
        "00:30:45"      # Less than an hour, no seconds in input but present in output logic? Input has SS.
                       # Wait, if input is HH:MM:SS, we always have components for H, M, S. 
    ]

    print("Input -> Output")
    print("-" * 40)
    
    for sample in samples:
        result = format_duration(sample)
        print(f"{sample} => {result}")