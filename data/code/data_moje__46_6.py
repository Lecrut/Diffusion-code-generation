SALARY_DATA = [45000, 52000, 48000, 61000, 55000, 72000, 68000]

def get_max_salary(data_list):
    max_value = data_list[0]
    for value in data_list[1:]:
        if value > max_value:
            max_value = value
    return max_value

if __name__ == '__main__':
    result = get_max_salary(SALARY_DATA)
    print(result)