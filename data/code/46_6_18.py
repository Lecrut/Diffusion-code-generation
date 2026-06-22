SALARY_DATA = [50000, 75000, 90000, 120000, 65000, 85000, 110000, 95000]

def get_max_salary(data_list):
    if not data_list:
        return 0
    max_val = data_list[0]
    for value in data_list:
        if value > max_val:
            max_val = value
    return max_val

if __name__ == '__main__':
    result = get_max_salary(SALARY_DATA)
    print(result)