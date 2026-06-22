def find_max_salary(nested_salaries):
    flat_salaries = []
    
    def flatten(item):
        if isinstance(item, list):
            for sub_item in item:
                flatten(sub_item)
        else:
            flat_salaries.append(item)
    
    flatten(nested_salaries)
    
    if not flat_salaries:
        return 0
    
    return max(flat_salaries)

if __name__ == '__main__':
    data = [
        [5000, 6000],
        [7000, 8000, [9000, 10000]],
        [12000]
    ]
    
    result = find_max_salary(data)
    print(result)