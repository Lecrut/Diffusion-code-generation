def find_max_element(data):
    if not data:
        raise ValueError("The list is empty")
    return max(data)

if __name__ == '__main__':
    sample_list = [10, 5, 20, 8, 15]
    print(find_max_element(sample_list))