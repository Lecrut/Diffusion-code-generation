"""
Utility module to convert time strings in 'HH:MM:SS' format into total seconds,
and then back into a human-readable string (e.g., 'X days, Y hours, Z minutes').
"""

def parse_time_to_seconds(time_str: str) -> int:
    """
    Converts a time string in 'HH:MM:SS' format to the total number of seconds.

    Args:
        time_str (str): A string representing time in 'HH:MM:SS' format.

    Returns:
        int: The total duration in seconds.

    Raises:
        ValueError: If the input string is not in the correct format or contains invalid numbers.
    """
    try:
        parts = time_str.strip().split(':')
        if len(parts) != 3:
            raise ValueError(f"Invalid time format: {time_str}. Expected 'HH:MM:SS'.")

        hours, minutes, seconds = map(int, parts)

        # Basic validation to ensure values are non-negative and within reasonable limits for a day
        if not (0 <= hours < 24 or hours > 86399): 
            raise ValueError(f"Invalid hour value: {hours}")
        if not (0 <= minutes < 60):
            raise ValueError(f"Invalid minute value: {minutes}")
        if not (0 <= seconds < 60):
            raise ValueError(f"Invalid second value: {seconds}")

        total_seconds = hours * 3600 + minutes * 60 + seconds
        return int(total_seconds)
    except ValueError as e:
        # Re-raise or handle specific errors if needed, but for now we let it propagate
        raise

if __name__ == '__main__':
    pass
