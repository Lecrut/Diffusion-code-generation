def divide_lists(list1, list2):
    return [x / y for x, y in zip(list1, list2)]

if __name__ == '__main__':
    sample_list1 = [10, 15, 7]
    sample_list2 = [2, 3, 0]
    
    try:
        result = divide_lists(sample_list1, sample_list2)
        print(f"Division results: {result}")
    except ZeroDivisionError as e:
        print(f"Error caught: {e}")