def convert_to_lower_and_swap_case(input_string):
    lowercased = input_string.lower()
    swapped_case = lowercased.swapcase()
    return swapped_case

if __name__ == '__main__':
    sample_input = 'Python Programming'
    result = convert_to_lower_and_swap_case(sample_input)
    print(result)