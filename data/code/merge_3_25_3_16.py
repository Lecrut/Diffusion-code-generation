def handle_invalid_input():
    """Prints a message indicating invalid input was entered."""
    print("Invalid input: please enter an integer.")

if __name__ == '__main__':
    # Sample hard-coded values to test the logic without user interaction
    sample_values = [0, 1, -5]

    for val in sample_values:
        try:
            num_input = int(val)
            
            if num_input == 0:
                print(f"The value {num_input} is zero.")
            else:
                print(f"The value {num_input} is not zero.")
                
        except ValueError:
            handle_invalid_input()