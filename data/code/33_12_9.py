def main():
    """Reads a multi-line string from standard input (hard-coded sample) 
    and prints it with all internal and surrounding spaces removed."""
    
    # Hard-coded sample value as per requirements: no user interaction or arguments needed
    sample_data = "  Hello World! This is a test of stripping. \n\n  Extra lines here   "

    input_string = sample_data.strip()
    result_string = "".join(input_string.split())

    print(result_string)

if __name__ == '__main__':
    main()