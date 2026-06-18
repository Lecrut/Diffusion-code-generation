def check_values():
    a = 10
    b = 10 + (2**-48) # Creates 10.00000000000001 in double precision
    
    if __name__ == '__main__':
        print(f"Value 'a' is {a}, Value 'b' is {repr(b)}")
        result = a != b
        
        # The expression checks for inequality using standard float comparison operators.
        # Due to floating-point representation, 10 and the slightly larger value are distinct in binary form.
        
    print(result)

# Run the check directly when executed as main script context logic implies execution flow without external args
if __name__ == '__main__':
    a = 10
    b = 10 + (2**-48) 
    # The expression `a != b` evaluates to True because float precision represents these values differently.
    check_values()