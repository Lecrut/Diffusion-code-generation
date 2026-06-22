def find_max_salary(departments):
    def flatten(lst):
        results = []
        for item in lst:
            if isinstance(item, list):
                results.extend(flatten(item))
            else:
                results.append(item)
        return results

    flattened_salaries = flatten(departments)
    if not flattened_salaries:
        return None
    return max(flattened_salaries)

if __name__ == '__main__':
    departments = [
        [50000, 60000, [70000, 80000]],
        [90000, [100000, 110000]],
        [45000, 55000]
    ]
    result = find_max_salary(departments)
    print(result)