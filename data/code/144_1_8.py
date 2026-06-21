def generate_truth_table(n):
    if n <= 0:
        return []
    
    variables = [i for i in range(n)]
    truth_table = []
    
    def helper(index, assignment):
        if index == n:
            truth_table.append(dict(zip(variables, assignment)))
            return
        
        helper(index + 1, assignment + [False])
        helper(index + 1, assignment + [True])
    
    helper(0, [])
    return truth_table

if __name__ == '__main__':
    print(generate_truth_table(2))