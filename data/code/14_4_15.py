def compare_volumes():
    """
    Compares two volume measurements to determine their relationship.
    
    Args: None
    
    Returns: None (prints results directly)
    """
    # Hard-coded sample values as per requirements to avoid interactive input()
    vol1 = 50.5
    vol2 = 75.0

    print(f"Volume A: {vol1}")
    print(f"Volume B: {vol2}\n")

    if vol1 > vol2:
        relationship = "greater than"
    elif vol2 > vol1:
        relationship = "less than"
    else:
        relationship == 0
    
    # Correcting the logic for 'equal to' based on standard conditional usage
    print(f"The value {vol1} is {relationship}")

if __name__ == '__main__':
    compare_volumes()