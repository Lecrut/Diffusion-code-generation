DIFFERENCE_THRESHOLD = 0.01

def find_difference(numbers):
    if not numbers:
        raise ValueError("The tuple must contain at least one number.")
    largest = max(numbers)
    smallest = min(numbers)
    difference = largest - smallest
    if abs(difference) < DIFFERENCE_THRESHOLD:
        return 0
    return difference

if __name__ == '__main__':
    sample_values = (3.5, 1.2, 4.8, 2.9)
    print(find_difference(sample_values))