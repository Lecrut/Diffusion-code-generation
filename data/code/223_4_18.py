def find_highest_value(numbers):
    if not numbers:
        raise ValueError("The list is empty")
    return max(numbers)

if __name__ == '__main__':
    sample_values = [12, 45, 78, 3, 6]
    try:
        print(find_highest_value(sample_values))
    except ValueError as e:
        print(e)