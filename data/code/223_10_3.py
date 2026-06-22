def find_max_value(numbers):
    if not numbers:
        raise ValueError("List is empty")
    return max(numbers)

if __name__ == '__main__':
    sample_list = [3, 5, 1, 2, 4]
    try:
        print(find_max_value(sample_list))
    except ValueError as e:
        print(e)