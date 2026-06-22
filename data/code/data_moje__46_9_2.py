def flatten_salaries(data, current_max=float('-inf')):
    if isinstance(data, (int, float)):
        return max(current_max, data)
    if isinstance(data, (list, tuple)):
        for item in data:
            current_max = flatten_salaries(item, current_max)
    return current_max

def max_salary(departments):
    return flatten_salaries(departments)

if __name__ == '__main__':
    departments = [
        {"Engineering": [100000, 120000, 110000]},
        {"Sales": [80000, 90000]},
        {"HR": [70000, 75000]},
        {"Finance": [[85000, 95000], 105000]}
    ]
    flat_departments = []
    for dept in departments:
        for key in dept:
            salaries = dept[key]
            flat_departments.append(salaries)
    result = max_salary(flat_departments)
    print(result)