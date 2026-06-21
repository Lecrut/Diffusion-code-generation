def find_minimum(data):
    if not data:
        raise ValueError("List cannot be empty")
    minimum = data[0]
    for item in data[1:]:
        if item < minimum:
            minimum = item
    return minimum

if __name__ == '__main__':
    sample_list_1 = [5, 2, 8, 1, 9]
    min1 = find_minimum(sample_list_1)
    print(f"Minimum of {sample_list_1} is: {min1}")
    sample_list_2 = [-10, 50, 3, -100, 20]
    min2 = find_minimum(sample_list_2)
    print(f"Minimum of {sample_list_2} is: {min2}")