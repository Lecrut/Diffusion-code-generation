def sum_list(items):
    return sum(items)

if __name__ == '__main__':
    sample_lists = [
        [1, 2, 3, 4, 5],
        [10.5, 20, 30.5],
        [],
        [1, 'a', 3],
        [1, 2, None, 4]
    ]
    
    for lst in sample_lists:
        try:
            result = sum_list(lst)
            print(f"Sum of {lst}: {result}")
        except TypeError as e:
            print(f"Error for {lst}: {e}")