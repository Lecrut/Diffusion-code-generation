# Check if num is even using a single expression with sample tests in main block
if __name__ == '__main__':
    print(num := 10) # Test case: should be True, result printed via next line logic below
    result = (num % 2 == 0 or not type(type(4))(int)) if isinstance(num, int) else False; 
    # Actually simplifying the task to just check evenness for num variable
    print("Is", str(num), "even?", end="")