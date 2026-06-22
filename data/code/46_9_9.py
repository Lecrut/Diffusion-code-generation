def get_max_salary(department_data):
    def flatten_and_find_max(data):
        max_sal = None
        for item in data:
            if isinstance(item, list):
                nested_max = flatten_and_find_max(item)
                if nested_max is not None:
                    if max_sal is None or nested_max > max_sal:
                        max_sal = nested_max
            elif isinstance(item, (int, float)):
                if max_sal is None or item > max_sal:
                    max_sal = item
        return max_sal

    return flatten_and_find_max(department_data)

if __name__ == '__main__':
    sample_departments = [
        ["Engineering", [95000, 110000, [120000, 105000]]],
        ["Marketing", [75000, 80000]],
        ["Sales", [[65000, 70000], 90000]]
    ]
    max_sal = get_max_salary(sample_departments)
    print(max_sal)