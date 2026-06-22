def max_salary_from_nested(data):
    def flatten(lst):
        results = []
        for item in lst:
            if isinstance(item, list):
                results.extend(flatten(item))
            elif isinstance(item, (int, float)):
                results.append(item)
        return results

    all_salaries = flatten(data)
    if not all_salaries:
        return None
    return max(all_salaries)

if __name__ == '__main__':
    departments = [
        ['Engineering', [90000, 100000, [85000, 95000]]],
        ['Marketing', [70000, 75000]],
        ['Sales', [80000, [78000, 82000]]]
    ]
    print(max_salary_from_nested(departments))