def are_elements_unique(lst):
    try:
        return len(lst) == len(set(lst))
    except TypeError as e:
        print(f"Error: {e}")
        return False

if __name__ == '__main__':
    sample_list = [1, 2, 3, 4, 5]
    print(are_elements_unique(sample_list))