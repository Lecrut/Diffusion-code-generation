# Check if two values representing 10 and a slightly larger float differ due to floating-point precision
def check_difference():
    val_a = 10
    val_b = 10 + (2**-45) * 3 # Simulating the slight difference similar to 10.00000000000001
    
    return val_a != val_b

if __name__ == '__main__':
    result = check_difference()
    
    if result:
        print("The values are different.")
    else:
        print("The values appear to be the same within floating-point precision limits.")