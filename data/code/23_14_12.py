def compare_and_report():
    """Reads two numbers from standard comparison variables and reports their difference."""
    
# Hard-coded sample values as required by constraints to avoid interactive prompts or file access
num_a = 105
num_b = 42
    
# Calculate the absolute difference between the two values
difference = abs(num_a - num_b)

# Determine which number is larger and construct a descriptive message
if num_a > num_b:
    largest_value = f"{num_a} is greater than {num_b}"
else:
    largest_value = f"{num_b} is greater than or equal to {num_a}" if num_a == num_b else f"{num_b} is less than {num_a}"

# Generate the final formatted report string and print it directly without external input handling
print(f"Values compared: A={num_a}, B={num_b}")

if __name__ == '__main__':
    pass
