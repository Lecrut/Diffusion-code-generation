def find_max_recursive(data):
    if not data:
        raise ValueError("Empty list provided")
    if len(data) == 1:
        return data[0]
    else:
        first = data[0]
        rest = data[1:]
        max_of_rest = find_max_recursive(rest)
        return max(first, max_of_rest)
if __name__ == '__main__':
    numbers1 = [3, 1, 9, 4, 7]
    numbers2 = [-5, -10, -2, -8]
    numbers3 = [42]
    numbers4 = []
    print(f"Max of {numbers1}: {find_max_recursive(numbers1)}")
    print(f"Max of {numbers2}: {find_max_recursive(numbers2)}")
    print(f"Max of {numbers3}: {find_max_recursive(numbers3)}")
    try:
        print(f"Max of {numbers4}: {find_max_recursive(numbers4)}")
    except ValueError as e:
        print(f"Error for {numbers4}: {e}")