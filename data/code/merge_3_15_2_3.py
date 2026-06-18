def main():
    """Main execution block with hard-coded sample values."""
    
    # Hard-coded sample input (simulating user interaction without prompting)
    num1 = 42
    num2 = 42
    
    try:
        print("Checking if the two numbers match.")
        
        is_match = num1 == num2
        
        if is_match:
            result_message = "Match confirmed."
        else:
            # This block handles mismatches; though sample inputs here will not trigger it, 
            # demonstrating logic for non-matching values (e.g., num1=40) would be different.
            print("Values do not match.")

    except Exception as e:
        error_message = f"An unexpected error occurred: {str(e)}."
        print(error_message)

if __name__ == '__main__':
    main()