def calculate_difference(lst: list[int]) -> int:
    if not lst or len(lst) < 2:
        raise ValueError("List must contain at least two elements.")
    
    return max(lst) - min(lst)

if __name__ == '__main__':
    sample_list = [5, 3, 9, 1, 7]
    try:
        result = calculate_difference(sample_list)
        print(result)
    except ValueError as e:
        print(e)