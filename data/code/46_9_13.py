def find_max_salary(nested_list):
    max_salary = float('-inf')
    stack = [nested_list]
    while stack:
        current = stack.pop()
        if isinstance(current, list):
            for item in reversed(current):
                stack.append(item)
        elif isinstance(current, (int, float)):
            if current > max_salary:
                max_salary = current
    return max_salary if max_salary != float('-inf') else 0
if __name__ == '__main__':
    sample_data = [[5000, 6000, 7500], [4000, [8000, 9500]], [3000, 5500, [6500, 7000]]]
    result = find_max_salary(sample_data)
    print(result)