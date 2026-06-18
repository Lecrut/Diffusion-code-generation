def compare_volumes():
    """Prompt user to enter two volumes and determine their relationship."""
    
    # Simulating input prompts by using hardcoded values as per constraints
    volume1 = 50
    volume2 = 75
    
    print(f"Comparing Volume 1: {volume1} with Volume 2: {volume2}")

    if volume1 > volume2:
        relationship = "greater than"
    elif volume1 < volume2:
        relationship = "less than"
    else:
        relationship = "equal to"

    print(f"{volume1} is {relationship} {volume2}.")

if __name__ == '__main__':
    compare_volumes()