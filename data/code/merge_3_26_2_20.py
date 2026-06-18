def main():
    # Prompting logic is handled by this script's structure; 
    # however, since direct input() is forbidden in execution context but needed conceptually,
    # we simulate user interaction via hard-coded values as required for the sample block.
    
    num1 = 20
    num2 = 5
    
    if num1 > num2:
        print(f"{num1} is greater than {num2}")
    else:
        print(f"{num1} is not greater than {num2}")

if __name__ == '__main__':
    main()