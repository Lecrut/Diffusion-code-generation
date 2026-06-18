def check_values(a, b):
    """Check if two values are equal considering both type and value."""
    return a == b and type(a) is type(b)

if __name__ == '__main__':
    # Hard-coded sample values to avoid any user input or prompts.
    val1 = 5
    val2 = "5"

    result = check_values(val1, val2)

    if result:
        print("The values are equal in both type and value.")
    else:
        print(f"The value {val1} is not exactly equal to {val2} because their types differ (int vs str).")