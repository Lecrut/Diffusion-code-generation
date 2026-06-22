THREE_NUMBERS = (10, 5, 20)

def find_the_middle_value_among_three_filter_valid(numbers):
    if len(numbers) != 3:
        raise ValueError("Input must be exactly three numbers")
    
    a, b, c = sorted(numbers)
    return b

if __name__ == '__main__':
    middle_value = find_the_middle_value_among_three_filter_valid(THREE_NUMBERS)
    print(middle_value)