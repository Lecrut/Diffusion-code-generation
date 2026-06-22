MAX_EMPTY_LIST_ERROR = "The list is empty"

def find_highest_value(numbers):
    if not numbers:
        raise ValueError(MAX_EMPTY_LIST_ERROR)
    return max(numbers)

if __name__ == '__main__':
    sample_values = [12, 45, 6, 90, 3]
    try:
        print(find_highest_value(sample_values))
    except ValueError as e:
        print(e)