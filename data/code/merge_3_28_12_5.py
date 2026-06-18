def main():
    # Simulate user input with hard-coded sample values to avoid interactive prompts
    num1 = 5.7
    num2 = 3.2
    
    try:
        val_a, val_b = float(num1), float(num2)
        
        if val_a > val_b:
            print(f"{val_a} is larger than {val_b}")
        elif val_b > val_a:
            print(f"{val_b} is larger than {val_a}")
        else:
            print("Both numbers are equal.")
    except ValueError as e:
        # Handle cases where input might not be valid floats, though our hard-coded values are safe here.
        print(f"Error processing inputs: {e}", file=__import__('sys').stderr)

if __name__ == '__main__':
    main()