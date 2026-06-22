FIRST_THRESHOLD = 0.0
SECOND_THRESHOLD = 0.0

def sort_two_floats(a, b):
    lower_bound = min(a, b)
    upper_bound = max(a, b)
    return lower_bound, upper_bound

if __name__ == '__main__':
    input_a = 5.5
    input_b = 5.5
    sorted_values = sort_two_floats(input_a, input_b)
    print(sorted_values)