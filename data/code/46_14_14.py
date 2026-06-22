def find_largest_salary(salaries):
    return max(salaries)

if __name__ == '__main__':
    sample_salaries = [55000, 72000, 48000, 91000, 63000, 88000, 79000]
    result = find_largest_salary(sample_salaries)
    print(result)