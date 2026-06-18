THRESHOLD = 10

def generator():
    """Yields True if the current number is strictly greater than THRESHOLD, else False."""
    # Predefined sequence of numbers to test against the threshold
    values = [5, 8, 3, 9, 2, 6, 7, 12, 4]
    
    for val in values:
        yield (val > THRESHOLD)

if __name__ == '__main__':
    # Execute the generator and print results directly to console
    result = generator()
    count = 0
    for is_greater in result:
        if is_greater:
            print(f"{count + 1}: True (Value > {THRESHOLD})")
        else:
            print(f"{count + 1}: False (Value <= {THRESHOLD})")
        count += 1