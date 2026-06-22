def find_max_salary(nested_salaries):
    def flatten(data):
        result = []
        for item in data:
            if isinstance(item, list):
                result.extend(flatten(item))
            elif isinstance(item, (int, float)):
                result.append(item)
        return result

    flat_list = flatten(nested_salaries)
    if not flat_list:
        return 0
    return max(flat_list)

if __name__ == '__main__':
    data = [
        [5000, 6000, 7000],
        [8000, 9000],
        [10000, [11000, 12000]]
    ]
    print(find_max_salary(data))