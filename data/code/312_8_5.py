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
    numbers1 = [3, 1, 4, 1, 5, 9, 2]
    numbers2 = [-10, -5, -20, -1]
    numbers3 = [42]
    numbers4 = []
    print(f"Maximum of {numbers1}: {find_max_recursive(numbers1)}")
    print(f"Maximum of {numbers2}: {find_max_recursive(numbers2)}")
    print(f"Maximum of {numbers3}: {find_max_recursive(numbers3)}")
    try:
        print(f"Maximum of {numbers4}: {find_max_recursive(numbers4)}")
    except ValueError as e:
        print(f"Error for {numbers4}: {e}")