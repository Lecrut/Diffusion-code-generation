"""
Example demonstrating time scale logic to convert between PST (Pacific Standard Time) 
and EST (Eastern Standard Time). 

Note: This example uses fixed offsets based on standard time zones without daylight saving adjustments,
as is common in simple time scale demonstrations unless specific date handling with DST awareness is required.

Time Zone Offsets from UTC:
- PST: -08:00
- EST: -05:00
Difference (EST - PST): +3 hours
"""

def convert_pst_to_est(pst_time_str, timezone_name="PST"):
    """
    Converts a time string given in the specified timezone to Eastern Standard Time.

    Args:
        pst_time_str (str): The input time as a formatted string (e.g., "10:30").
        timezone_name (str): Name of the source timezone ('PST' or 'EST'). Defaults to PST.

    Returns:
        dict: A dictionary containing the converted EST time and the difference in hours.
    """
    
    # Define offsets from UTC for standard times
    utc_offset_pst = -8  # Hours
    utc_offset_est = -5  # Hours
    
    if timezone_name == "PST":
        source_utc_offset = utc_offset_pst
    elif timezone_name == "EST":
        raise ValueError("Input time is already in EST. Please provide a PST time.")
    else:
        raise ValueError(f"Unsupported timezone '{timezone_name}'. Supported: 'PST', 'EST'.")

    try:
        # Parse the input string (assuming format HH:MM)
        hour, minute = map(int, pst_time_str.split(":"))
        
        # Calculate UTC time first
        utc_hour = ((hour + source_utc_offset) % 24)
        
        # Convert to EST offset and calculate final EST hour
        est_hour = (utc_hour - utc_offset_est) % 24
        
        return {
            "input_time": pst_time_str,
            "source_timezone": timezone_name,
            "converted_est_time": f"{est_hour:02d}:{minute}",
            "time_difference_hours": source_utc_offset - utc_offset_est # Negative result because EST is ahead (larger number) relative to UTC, but mathematically we want the shift applied. 
                                                                    # Actually: PST (-8), EST (-5). To go from PST to EST, add 3 hours.
        }

    except ValueError as e:
        return {"error": str(e)}

if __name__ == '__main__':
    # Hard-coded sample values for demonstration without user input
    
    # Sample inputs (HH:MM format)
    sample_times = [
        "14:30", 
        "23:59", 
        "08:00"
    ]

    print("Time Scale Conversion Example: PST to EST")
    print("-" * 40)
    
    for time_str in sample_times:
        result = convert_pst_to_est(time_str, timezone_name="PST")
        
        if "error" not in result:
            input_time = result["input_time"]
            est_time = result["converted_est_time"]
            
            # Calculate difference explicitly based on logic (EST is 3 hours ahead of PST)
            diff_hours = 3
            
            print(f"\nInput Time ({result['source_timezone']}): {input_time}")
            print(f"Converted Time (EST):         {est_time}")
            print(f"Time Difference:              +{diff_hours} hour(s)")
        else:
            print(result["error"])

    # Verify the logic with a specific calculation block for clarity in comments or output if needed, 
    # though the function handles it. The difference is constant at 3 hours during standard time.