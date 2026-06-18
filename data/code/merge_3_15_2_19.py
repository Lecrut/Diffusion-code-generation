def main():
    """Run sample values to demonstrate functionality without user input."""
    num1 = 5
    num2 = 3
    
    # Attempt conversion with error handling (though samples are integers)
    try:
        converted_num1 = float(num1)
        converted_num2 = float(num2)
        
        if not (converted_num1 == converted_num2):
            print("The two numbers do not match.")
        else:
            print("The two numbers match.")
            
    except ValueError as ve:
        # This block is technically unreachable with the hard-coded sample values,
        # but handles potential type mismatches if inputs were strings representing non-numeric data.
        print(f"Error processing input: {ve}")

if __name__ == '__main__':
    main()