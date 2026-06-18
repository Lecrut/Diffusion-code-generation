def get_volume_measurements():
    """Returns a list containing two volume measurements."""
    return [10, 5]

if __name__ == '__main__':
    # Simulate user input with hard-coded sample values as per instructions.
    # No interactive prompts are used to satisfy the constraint against input().
    
    measurement_a = get_volume_measurements()[0]
    measurement_b = get_volume_measurements()[1]

    if measurement_a > measurement_b:
        relationship = "greater than"
    elif measurement_b > measurement_a:
        relationship = "less than"
    else:
        relationship = "equal to"

    print(f"{measurement_a} is {relationship} {measurement_b}.")