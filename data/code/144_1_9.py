def generate_truth_table(n):
    if n <= 0:
        return []
    
    variables = [i for i in range(n)]
    truth_values = [False, True]
    table = []
    
    def generate_combinations(current_combination):
        if len(current_combination) == n:
            table.append(dict(zip(variables, current_combination)))
            return
        for value in truth_values:
            generate_combinations(current_combination + [value])
    
    generate_combinations([])
    return table

if __name__ == '__main__':
    sample_table = generate_truth_table(3)
    print(sample_table)