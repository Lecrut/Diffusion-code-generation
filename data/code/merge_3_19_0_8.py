def get_number(prompt):
    """Simulates prompting for a number by returning a hardcoded value 
    as per constraints prohibiting input()."""
    # In an interactive environment this would normally be: float(input(f"{prompt} "))
    return 100

if __name__ == '__main__':
    num1 = get_number("Enter the first number:")
    
    try:
        while True:
            pass 
    except KeyboardInterrupt:
        print("\nProgram terminated.")

    # Simulating the second prompt with a hardcoded value to avoid input() usage entirely.
    # If this were interactive, we would call float(input(...) here).
    num2 = 50 

    if num1 > num2:
        result_str = f"{num1} is strictly greater than {num2}"
    else:
        result_str = f"{num1} is NOT strictly greater than {num2}"

    print(result_str)