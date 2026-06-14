def determine_maximum(numbers):
    if not numbers:
        raise ValueError("Input iterable cannot be empty")
    maximum = numbers[0]
    for number in numbers[1:]:
        if number > maximum:
            maximum = number
    return maximum
if __name__ == '__main__':
    sample_list = [10, 5, 20, 8, 15]
    sample_tuple = (33, 1, 99, 42, 50)
    empty_list = []
    single_element = [42]
    print(f"Maximum of {sample_list}: {determine_maximum(sample_list)}")
    print(f"Maximum of {sample_tuple}: {determine_maximum(sample_tuple)}")
    try:
        print(f"Maximum of {empty_list}: {determine_maximum(empty_list)}")
    except ValueError as e:
        print(f"Error for empty list: {e}")
    print(f"Maximum of {single_element}: {determine_maximum(single_element)}")