"""
Time Scale Conversion Example: PST to EST
This module demonstrates converting a timestamp between Pacific Standard Time (PST) 
and Eastern Standard Time (EST). Since both are UTC-8 during standard time, 
the difference is zero hours in this specific scenario. The logic handles the offset calculation explicitly.

Note: If daylight saving were active, offsets would differ (-7 for PST/EDT and -4 for EST),
but here we strictly use Standard Time offsets as per the task requirement of "PST to EST".
"""

# Define fixed UTC offsets in hours for standard time zones
PST_OFFSET = -8  # Pacific Standard Time is UTC-8
EST_OFFSET = -5  # Eastern Standard Time is UTC-5

def convert_timezone(hour: int, minute: int) -> tuple[int, int]:
    """
    Converts a given hour and minute from PST to EST based on fixed offsets.

    Args:
        hour (int): The input hour in PST format.
        minute (int): The input minute value.

    Returns:
        tuple[int, int]: A tuple containing the converted hour and minute for EST.
                         If seconds are needed or negative results from subtraction occur, 
                         this function assumes a simple addition of offset difference to avoid complex borrowing logic 
                         unless explicitly required by advanced datetime libraries which we simulate here with pure math.

    Logic:
        1. Calculate the time difference in hours between PST and EST (EST - PST).
           Difference = (-5) - (-8) = +3 hours.
        2. Add this difference to the input hour.
        3. Handle minute overflow or underflow if necessary, though simple addition usually handles it directly 
           with modulo arithmetic for a clean result.

    Example:
        Input (PST): 10:45 -> Output (EST): 13:45 (+3 hours)
    """
    # Calculate time difference in hours between the two zones
    offset_hours = EST_OFFSET - PST_OFFSET
    
    # Convert input hour and minute to total minutes from midnight
    total_minutes_pst = (hour * 60) + minute

    # Add the timezone offset difference to convert to EST
    total_minutes_est = total_minutes_pst + (offset_hours * 60)

    # Calculate new hour, minute and handle potential day boundary crossing if needed for display logic
    final_hour = int(total_minutes_est // 60) % 24
    final_minute = int(total_minutes_est % 60) or 0
    
    return final_hour, final_minute

if __name__ == '__main__':
    # Hard-coded sample values representing a time in PST (e.g., 10:30 AM Pacific Standard Time)
    input_pst_time = {
        "hour": 14, 
        "minute": 35
    }

    print(f"Original Time (PST): {input_pst_time['hour']:02d}:{input_pst_time['minute']:02d}")

    # Perform the conversion logic
    converted_hour, converted_minute = convert_timezone(input_pst_time["hour"], input_pst_time["minute"])

    print(f"Converted Time (EST): {converted_hour:02d}:{converted_minute:02d}")

    # Calculate and display the resulting time difference in hours
    diff_hours = EST_OFFSET - PST_OFFSET
    
    result_difference_message = f"The resulting time difference between PST and EST is a gain of {diff_hours} hour(s)." if diff_hours > 0 else f"The resulting time difference between PST and EST is a loss of {-diff_hours} hour(s)."

    print(result_difference_message)