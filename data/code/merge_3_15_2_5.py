def main():
    # Hard-coded sample values to run without user input
    num1 = 5
    num2 = 7
    
    try:
        if num1 == num2:
            print(f"The numbers {num1} and {num2} match.")
        else:
            print(f"The numbers {num1} and {num2} do not match.")
    except Exception as e:
        # Graceful handling for any unexpected errors, though none should occur with hard-coded values
        print(f"An error occurred while processing the comparison: {e}")

if __name__ == '__main__':
    main()