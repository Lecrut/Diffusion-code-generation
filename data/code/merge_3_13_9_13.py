"""
Time Scale Conversion Example: PST to EST
This module demonstrates converting a time from Pacific Standard Time (PST) 
to Eastern Standard Time (EST) using fixed offset logic, as no external timezone libraries are required.
Note: This example uses standard offsets (-8 for PST and -5 for EST). It does not account for Daylight Saving Time adjustments dynamically but represents the core conversion logic requested.

Standard Offsets from UTC:
- PST (Pacific Standard Time): UTC-8
- EST (Eastern Standard Time): UTC-5

Difference Calculation:
EST is 3 hours ahead of PST during standard time periods.
"""

def convert_pst_to_est(pst_hour, pst_minute=0):
    """
    Converts a given hour and minute in PST to the corresponding time in EST.
    
    Args:
        pst_hour (int): Hour value in PST range [0-23].
        pst_minute (int): Minute value in PST range [0-59], defaults to 0.
        
    Returns:
        tuple: A tuple containing (est_hour, est_minute).
               If the conversion crosses midnight, it returns a negative hour 
               indicating the previous day's time or adjusts accordingly based on context.
    """
    
    # Define offsets from UTC in hours
    pst_offset = -8  # PST is UTC-8
    est_offset = -5  # EST is UTC-5
    
    # Calculate difference between two zones (EST - PST)
    zone_diff_hours = est_offset - pst_offset  # Should be +3
    
    # Convert to total minutes for easier calculation with potential day rollover
    pst_total_minutes = pst_hour * 60 + pst_minute
    
    # Add the time difference in minutes
    est_total_minutes = pst_total_minutes + (zone_diff_hours * 60)
    
    # Calculate new hour and minute, handling negative values or overflow to next/previous day if needed. 
    # Since we are just converting within a single logical cycle without date context:
    est_hour = int(est_total_minutes // 60) % 24
    
    # Handle cases where the result might be less than zero (indicating previous day relative to input start point logic)
    if est_hour < 0:
        est_hour += 24
        
    est_minute = abs(est_total_minutes - (est_hour * 60))
    
    return est_hour, est_minute

if __name__ == '__main__':
    # Hard-coded sample values as per requirements. No user input or external files used.
    pst_time_value = "14:30"  # PST Time
    
    try:
        parts = pst_time_value.split(':')
        if len(parts) != 2:
            raise ValueError("Invalid time format")
        
        hour_str, minute_str = parts
        
        pst_hour = int(hour_str)
        pst_minute = int(minute_str)
        
        # Perform conversion logic
        est_hour, est_minute = convert_pst_to_est(pst_hour, pst_minute)
        
        # Format output strings for clarity
        if est_hour < 0:
            formatted_est_time = f"{est_hour % 24}:{str(est_minute).zfill(2)}"
        else:
            formatted_est_time = f"{abs(est_hour):02d}:{str(est_minute).zfill(2)}"

        # Calculate and display the time difference in hours
        diff_hours = zone_diff_hours
        
        print(f"PST Time Input: {pst_time_value}")
        print(f"Converted EST Time: {formatted_est_time} ({abs(diff_hours):02d}:{str(abs(zone_diff_hours)).zfill(1)}h)")
        
    except ValueError as ve:
        print(f"Error processing time input: {ve}")