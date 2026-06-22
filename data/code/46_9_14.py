def find_max_salary(data):
    def flatten(nested):
        for item in nested:
            if isinstance(item, (list, tuple)):
                yield from flatten(item)
            else:
                yield item

    salaries = flatten(data)
    return max(salaries)

if __name__ == '__main__':
    departments = [
        ["Engineering", [120000, 150000, 110000]],
        ["Marketing", [90000, 85000]],
        ["Sales", [100000, [95000, 105000]]]
    ]
    print(find_max_salary(departments))