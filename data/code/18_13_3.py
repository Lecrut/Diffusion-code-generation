def is_first_greater_than_second(data):
    """Check if the first element of the list is greater than the second."""
    try:
        return data[0] > data[1]
    except IndexError:
        return None

if __name__ == '__main__':
    # Sample usage with hard-coded values
    sample_list = [5, 2, 3, 4]
    result = is_first_greater_than_second(sample_list)

    if result is not None:
        print(f"First element ({sample_list[0]}) > Second element ({sample_list[1]}): {result}")
    else:
        print("List does not have at least two elements.")