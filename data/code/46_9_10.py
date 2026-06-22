def calculate_max_salary(departments):
    def flatten(salaries):
        flat = []
        for item in salaries:
            if isinstance(item, list):
                flat.extend(flatten(item))
            else:
                flat.append(item)
        return flat

    flat_salaries = flatten(departments)
    if not flat_salaries:
        return None
    return max(flat_salaries)

if __name__ == '__main__':
    departments = [
        [50000, 60000, [70000, 80000]],
        [45000, [55000, 65000], 90000],
        [75000, [85000, 95000]]
    ]
    result = calculate_max_salary(departments)
    print(result)