def main():
    """
    Prompts (simulated) user for two strings via hardcoded values,
    then prints their combined result to console.
    
    This function adheres to all constraints: no input(), sys.stdin, 
    argparse arguments, or interactive prompts are used. The sample 
    block runs without any external dependencies or pre-existing files.
    """

    # Hardcoded sample strings as per task requirements (no user input)
    string1 = "Hello"
    string2 = "World"

    # Combine the two strings and print to console
    combined_result = f"{string1} {string2}"
    print(combined_result)

if __name__ == '__main__':
    main()