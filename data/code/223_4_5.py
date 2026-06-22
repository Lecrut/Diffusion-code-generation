def get_highest_value(numbers):
    if not numbers:
        raise ValueError("The list is empty")
    return max(numbers)

if __name__ == '__main__':
    sample_list = [12, 4, 55, 3]
    try:
        print(get_highest_value(sample_list))
    except ValueError as e:
        print(e)