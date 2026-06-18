# Single line expression to find length of 'Hello World' with explanation logic embedded via print in if block
length = len('Hello World') # This uses Python's built-in len() function which returns the number of characters (21) including space and case sensitivity matters.
if __name__ == '__main__':
    sample_string = "Hello World"  # Hard-coded sample value as per requirements, no user input needed
    result_length = len(sample_string)
    print(f"The length of '{sample_string}' is {result_length} characters.")