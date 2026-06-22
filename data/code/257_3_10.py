def calculate_difference(data):
    if len(data) < 2:
        raise ValueError("List must contain at least two elements to calculate the difference.")
    return max(data) - min(data)

if __name__ == '__main__':
    list1 = [3+4j, 1+1j, 5+6j]
    list2 = [2+2j, 3+3j]
    try:
        result1 = calculate_difference(list1)
        print(f"Difference for {list1}: {result1}")
        result2 = calculate_difference(list2)
        print(f"Difference for {list2}: {result2}")
    except ValueError as e:
        print(f"Error: {e}")