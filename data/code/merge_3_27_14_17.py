def main():
    val1 = 10
    val2 = 10.00000000000001
    
    # Check if values differ using direct equality comparison with a small epsilon tolerance for float precision issues, 
    # but note: the prompt specifically asks to check IF they are different. Since one is int and other is float slightly greater than 10,
    # standard != will return True because 10 < 10.00000000000001. However, often "different" in numeric contexts implies 
    # considering floating point noise. Here we follow the literal interpretation of inequality for these specific numbers.
    
    if val1 != val2:
        print("Values are different")
    else:
        print("Values are equal")

if __name__ == '__main__':
    main()