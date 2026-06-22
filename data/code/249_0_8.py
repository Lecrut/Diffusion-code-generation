MAX_VALUE_ERROR = "Cannot find maximum in an empty list"

def find_max_value(numbers):
    if not numbers:
        raise ValueError(MAX_VALUE_ERROR)
    return max(numbers)

if __name__ == '__main__':
    sample_values = [3, 5, 1, 2, 4]
    print(find_max_value(sample_values))
    empty_list = []
    try:
        print(find_max_value(empty_list))
    except ValueError as e:
        print(e)