import math

EPSILON = 1e-9

def compare_lengths(length1, length2):
    if math.isclose(length1, length2, abs_tol=EPSILON):
        return None
    elif length1 > length2:
        return length1
    else:
        return length2

if __name__ == '__main__':
    sample_length1 = 3.141592653589793
    sample_length2 = 3.141592653589794
    result = compare_lengths(sample_length1, sample_length2)
    if result is None:
        print("The lengths are approximately equal.")
    else:
        print(f"The greater length is: {result}")