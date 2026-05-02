def compare_lengths(length1, length2):
    if isinstance(length1, (int, float)) and isinstance(length2, (int, float)):
        difference = abs(length1 - length2)
        print(f"Length 1: {length1}")
        print(f"Length 2: {length2}")
        print(f"The difference between the two lengths is: {difference}")
    else:
        print("Error: Both inputs must be numeric values.")
if __name__ == '__main__':
    sample_length1 = 15.5
    sample_length2 = 22.3
    compare_lengths(sample_length1, sample_length2)