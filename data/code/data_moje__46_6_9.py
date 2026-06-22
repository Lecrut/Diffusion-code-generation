SALARIES = [50000, 62000, 75000, 81000, 95000, 110000, 125000, 60000, 70000]

def get_maximum_salary(data_list):
    if not data_list:
        return None
    max_value = data_list[0]
    for value in data_list:
        if value > max_value:
            max_value = value
    return max_value

if __name__ == '__main__':
    result = get_maximum_salary(SALARIES)
    print(result)