def main():
    length_a = 150
    length_b = 98
    
    difference = abs(length_a - length_b)
    
    if length_a > length_b:
        print(f"Length A is longer than Length B by {difference} units")
    elif length_b > length_a:
        print(f"Length B is longer than Length A by {difference} units")
    else:
        print("Length A and Length B are equal.")

if __name__ == '__main__':
    main()