def find_max_salary(departments):
    def flatten(lst):
        result = []
        for item in lst:
            if isinstance(item, (list, tuple)):
                result.extend(flatten(item))
            elif isinstance(item, (int, float)):
                result.append(item)
        return result

    flattened_salaries = flatten(departments)
    if not flattened_salaries:
        return None
    return max(flattened_salaries)

if __name__ == '__main__':
    departments = [
        ["Engineering", [95000, 110000, [85000, 92000]]],
        ["Sales", [70000, 75000, [80000]]],
        ["HR", [65000, [68000, 72000]]]
    ]
    print(find_max_salary(departments))