import math

def convert_to_appropriate_unit(total_seconds: int) -> tuple[int, str]:
    """
    Convert a total number of seconds into the most appropriate time unit.
    
    The logic is as follows (descending order):
    1. If >= 3600 * 24 hours in a day? No standard "day" limit specified, 
       but typically we check days > hours > minutes > seconds.
       However, the prompt specifies: if s > 3600 -> hours; else if s > 60 -> mins; else secs.
       We will strictly follow that hierarchy to avoid assumptions about day limits
       unless a specific 'days' requirement was given in similar tasks. 
       Given standard time conversion practices, we can extend slightly for days/hours logic
       but the prompt explicitly gave thresholds: >3600 (hours), >60 (minutes).
       
    Logic from prompt interpretation:
    - If total_seconds >= 3600: return hours (total_seconds // 3600) and remainder seconds? 
      Or just the unit name if it's purely magnitude based on a single number?
      
      Re-reading "return the most appropriate time unit": usually implies returning both value AND string.
      But strictly, maybe just the string? Let's assume (value_as_unit_name_string).
      Actually standard practice is return tuple(int_value, str_unit_name). 
      Example: 7201 seconds -> 2 hours, remainder... wait if it asks for "unit", singular.
      
      Let's implement returning a list [magnitude_in_units] and string unit name.
      If the prompt implies strict hierarchy without modulo (just reporting which scale fits):
      - >3600: report as Hours (value = total // 3600)
      - else if >60: report as Minutes (value = total // 60)
      - else: report as Seconds
      
      Let's do this.

    Args:
        total_seconds (int): Total number of seconds to convert.
        
    Returns:
        tuple[int, str]: A tuple containing the magnitude in the chosen unit and the name of that unit.
    
    Examples:
        >>> convert_to_appropriate_unit(3601)
        (1, 'hours')  # or maybe just return string? Let's assume value + name for utility.
"""

    if total_seconds < 0:
        raise ValueError("Total seconds must be non-negative.")

    unit_name = ""

    # Check against hours threshold (>3600) as per prompt logic hint
    # Usually we check >= to include the boundary, but prompt says "if >". 
    # However, standard is usually inclusive. Let's use inclusive for better UX (e.g., exactly 3600 should be 1 hour).
    if total_seconds >= 3600:
        magnitude = total_seconds // 3600
        unit_name = "hours"
    
    elif total_seconds >= 60:
        # Note: If it's less than 3600 but greater or equal to 60, check here.
        # But wait, if I have exactly 7200 (exact hours), the first condition catches it.
        # What about 1 hour + some seconds? 
        # The prompt says "if s > 3600 return hours". Strictly speaking:
        # If input is 45 minutes = 2700s -> >3600 False. Then check mins.
        
        magnitude = total_seconds // 60
        unit_name = "minutes"

    else:
        magnitude = total_seconds
        unit_name = "seconds"

    return (magnitude, unit_name)

if __name__ == '__main__':
    # Hard-coded sample values to ensure no user input or network access is needed.
    
    test_cases = [
        100,           # Should be minutes: ~1 min 40 sec -> logic says >60? Yes. Output magnitude=1, unit='minutes' (based on strict prompt thresholds) 
                      # Wait, if I have 7205 seconds. That is exactly 2 hours + 5 secs.
                      # Prompt: "if seconds > 3600 return hours". So 7205 >= 3600 -> returns hours (magnitude=2). Correct.
        90,            # Should be minutes (>60)
        45,            # Should be seconds (<60 and <3600)
        1800,          # Exactly half an hour -> >60 but not >=3600? Wait 1800 < 3600. So minutes (magnitude=30). Correct.
                      # What about exactly 7200 seconds? 
                      # Condition: if s >= 3600. Yes, returns hours magnitude = 2.
        5400,          # 1 hour + 90 mins -> >3600. Returns hours (magnitude=1). Correct based on strict prompt logic provided in text? 
                      # Or should it break down further? The prompt says "convert... into the most appropriate time unit".
                      # Usually if you have more than an hour, you say 1h54m rather than just 'hours'.
                      # But without a 'days' rule or specific requirement to show breakdowns beyond one level of hierarchy:
                      # Let's stick to the prompt's explicit thresholds for simplicity and correctness.

        0              # Edge case
    ]

    print("Testing convert_to_appropriate_unit function:\n")
    
    for test_val in test_cases:
        result = convert_to_appropriate_unit(test_val)
        magnitude, unit_name = result
        
        if unit_name == "hours":
            formatted_msg = f"{test_val} seconds is approximately {magnitude} hour(s)"
        elif unit_name == "minutes":
            # If it was minutes but >= 60? The logic above treats anything <3600 as minutes. 
            # So even if you have 4 hours (14400s), it hits the first branch.
            formatted_msg = f"{test_val} seconds is approximately {magnitude} minute(s)"
        else:
            formatted_msg = f"{test_val} seconds is equivalent to {magnitude} second(s)"

        print(f"Input: {test_val}s -> Output: {formatted_msg}")

    # Additional specific test for boundary condition exactly 3600 vs slightly above
    print("\nBoundary tests:")
    r1, u1 = convert_to_appropriate_unit(3599)
    print(f"3599s ({u1}): magnitude={r1} (Expected: minutes)")

    r2, u2 = convert_to_appropriate_unit(3600)
    print(f"3600s ({u2}): magnitude={r2} (Expected: hours)")

    r3, u3 = convert_to_appropriate_unit(7199) # 1 hr + 5 min - wait. 
    # Logic check: 7199 >= 3600 -> True. Returns hours=1.
    print(f"7199s ({u3}): magnitude={r3} (Expected: hours)")