LARGEST_THRESHOLD = 0
def determine_maximum(first, second, third):
    current_max = first
    if second > current_max:
        current_max = second
    if third > current_max:
        current_max = third
    return current_max
if __name__ == '__main__':
    value_a = 10.5
    value_b = 10.5
    value_c = 15.2
    print(determine_maximum(value_a, value_b, value_c))