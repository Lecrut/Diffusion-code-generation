def get_max_salary(nested_structure):
    flat_list = []
    def flatten(lst):
        for item in lst:
            if isinstance(item, list):
                flatten(item)
            else:
                flat_list.append(item)
    flatten(nested_structure)
    if not flat_list:
        return 0
    return max(flat_list)

if __name__ == '__main__':
    data = [
        [1000, 2000, 3000],
        [4000, [5000, 6000]],
        [7000, 8000, [9000, [10000]]]
    ]
    result = get_max_salary(data)
    print(result)