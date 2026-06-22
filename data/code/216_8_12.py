def find_middle(data):
    n = len(data)
    if n == 0:
        raise ValueError("List is empty")
    middle_index = n // 2
    return data[middle_index]

if __name__ == '__main__':
    try:
        sample_list = [3, 1, 4, 1, 5, 9, 2, 6, 5]
        result = find_middle(sample_list)
        print(f"The middle value is: {result}")
    except ValueError as e:
        print(e)