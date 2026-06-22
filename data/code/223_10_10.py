def find_maximum(data):
    if not data:
        raise ValueError("Input list cannot be empty")
    return max(data)

if __name__ == '__main__':
    sample_list = [10, 20, 30, 40, 50]
    another_list = [-1, -2, -3, -4, -5]
    single_element_list = [7]
    empty_list = []
    
    print(f"Maximum of {sample_list}: {find_maximum(sample_list)}")
    print(f"Maximum of {another_list}: {find_maximum(another_list)}")
    print(f"Maximum of {single_element_list}: {find_maximum(single_element_list)}")
    try:
        find_maximum(empty_list)
    except ValueError as e:
        print(e)