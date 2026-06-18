# Single line expression to find length of 'Hello World' with explanation in docstring
length = len('Hello World')  # The mechanism is Python's built-in len() function which returns the number of characters (or items) in a sequence; for strings it counts each character including spaces.

if __name__ == '__main__':
    sample_string = 'Hello World'
    result_length = len(sample_string)
    print(f"Length of '{sample_string}' is {result_length}")