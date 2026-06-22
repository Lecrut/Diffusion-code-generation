MAX_VALUE_ERROR = "The list is empty"

def get_highest_value(numbers):
    if not numbers:
        raise ValueError(MAX_VALUE_ERROR)
    return max(numbers)

if __name__ == '__main__':
    sample_list = [12, 34, 56, 78, 90]
    try:
        print(get_highest_value(sample_list))
    except ValueError as e:
        print(e)