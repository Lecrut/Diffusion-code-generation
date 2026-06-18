import sys

# Lambda to check if an integer is negative
is_negative = lambda x: x < 0

if __name__ == '__main__':
    # Hard-coded test cases without user input or command-line arguments
    test_cases = [1, -5, 0, -42]
    
    for num in test_cases:
        result = is_negative(num)
        print(f"Number {num} -> Is negative? {result}")

# Output example (to be verified when run):
# Number 1 -> Is negative? False
# Number -5 -> Is negative? True
# Number 0 -> Is negative? False
# Number -42 -> Is negative? True