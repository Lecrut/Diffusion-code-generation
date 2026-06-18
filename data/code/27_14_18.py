# Task: Check if 10 and 10.00000000000001 are different using a concise Python expression.
# Principle: Floating-point arithmetic can introduce small errors due to binary representation,
# so direct equality checks (`==`) may fail even for seemingly identical values when they have minor discrepancies.
# However, 10 and the specific value provided (10 + tiny_epsilon) are mathematically distinct by more than machine epsilon,
# meaning `!=` will correctly identify them as different without needing tolerance thresholds in this case.

def check_difference():
    """Check if two float values are considered different."""
    val_a = 10
    val_b = 10.00000000000001
    
    # Return True only if the condition differs from False, making it idiomatic and concise
    return bool(val_a != val_b)

if __name__ == '__main__':
    result = check_difference()
    print(f"Are 10 and {val_b} different? {'Yes' if result else 'No'}")