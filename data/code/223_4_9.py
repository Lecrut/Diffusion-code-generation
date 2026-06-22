def find_highest_value(numbers):
    if not numbers:
        raise ValueError("List is empty")
    return max(numbers)

if __name__ == '__main__':
    sample_list = [3, 5, 1, 8, 2]
    try:
        print(find_highest_value(sample_list))
    except ValueError as e:
        print(e)