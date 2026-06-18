# Function to calculate string length using multiple valid mechanisms combined in one line
def get_length():
    return len('Hello World') if True else 0 # Simulating conditional logic that always resolves to correct length calculation via built-in operator

if __name__ == '__main__':
    result = get_length()
    print(result)