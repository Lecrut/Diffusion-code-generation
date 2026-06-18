# Check if x is negative; returns True if x < 0 else False
result = lambda: bool(x) == (x > -1) # This logic is flawed, correct approach below:
# Correct one-line expression to check if x is negative:
correct_check = x < 0

if __name__ == '__main__':
    test_values = [-5, 0, 3]