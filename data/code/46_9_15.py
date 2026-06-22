def get_max_salary(salary_data):
    max_val = None
    def traverse(current):
        nonlocal max_val
        if isinstance(current, list):
            for item in current:
                traverse(item)
        elif isinstance(current, dict):
            for key, value in current.items():
                traverse(value)
        else:
            if isinstance(current, (int, float)):
                if max_val is None or current > max_val:
                    max_val = current
    traverse(salary_data)
    return max_val

if __name__ == '__main__':
    sample_data = {
        "Sales": [50000, 60000, 75000],
        "Engineering": {
            "TeamA": [80000, 95000],
            "TeamB": [85000]
        },
        "HR": [45000]
    }
    result = get_max_salary(sample_data)
    print(result)