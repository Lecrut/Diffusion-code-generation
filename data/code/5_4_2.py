# Script to compare two length measurements using conditional statements

def main():
    # Define sample variables for length measurements
    length_a = 150
    length_b = 87
    
    print(f"Length A is {length_a} units and Length B is {length_b} units.")
    
    if length_a > length_b:
        difference = length_a - length_b
        sentence = f"Length A is longer than Length B by {difference} units."
    elif length_b > length_a:
        difference = length_b - length_a
        sentence = f"Length B is longer than Length A by {difference} units."
    else:
        sentence = "Both lengths are equal."
    
    print(sentence)

if __name__ == '__main__':
    main()