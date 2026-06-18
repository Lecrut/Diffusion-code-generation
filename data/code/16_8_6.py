import sys

def process_number(value: int) -> bool:
    """Check if a number is positive."""
    return value > 0

if __name__ == '__main__':
    sample_values = [1, -5, 0, 42]
    
    for num in sample_values:
        result = process_number(num)
        print(f"{num} -> {result}")