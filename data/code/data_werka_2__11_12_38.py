def calculate_length_ratio(list1, list2):
    if len(list2) == 0:
        raise ValueError("The second list cannot be empty.")
    return float(len(list1)) / len(list2)

if __name__ == '__main__':
    list1 = [1, 2, 3, 4, 5]
    list2 = [6, 7, 8]
    ratio = calculate_length_ratio(list1, list2)
    print(ratio)