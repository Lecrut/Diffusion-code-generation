import re

def parse_and_evaluate(text1, text2):
    conditions = []
    
    def extract_conditions(text):
        statements = re.findall(r"if\s+(.*?):\s*(.*)", text, re.DOTALL)
        for _, condition_str in statements:
            conditions.append(condition_str.strip())
    
    extract_conditions(text1)
    extract_conditions(text2)
    
    if not conditions:
        return False
    
    all_variables = set()
    for cond in conditions:
        match = re.findall(r'[A-Za-z_]\w*', cond)
        all_variables.update(match)
    
    variable_list = sorted(list(all_variables))
    num_vars = len(variable_list)
    
    for assignment_tuple in product([False, True], repeat=num_vars):
        assignments = dict(zip(variable_list, assignment_tuple))
        truth_values = []
        for condition in conditions:
            try:
                eval_condition = condition
                for var, val in assignments.items():
                    eval_condition = eval_condition.replace(var, str(val).lower())
                if eval(eval_condition):
                    truth_values.append(True)
                else:
                    truth_values.append(False)
            except Exception as e:
                return False
        
        if len(set(truth_values)) == 1 and not truth_values[0]:
            return True
    
    return False

if __name__ == '__main__':
    sample_string_1 = "if x > 5: print('A')"
    sample_string_2 = "if y < 10 and z > 20: print('B')"
    sample_string_3 = "if a > 10 and a < 5: print('C')"
    sample_string_4 = "if x > 5 and not (x > 5): print('D')"
    sample_string_5 = "if p or q: print('E')"
    
    print(parse_and_evaluate(sample_string_1, sample_string_2))
    print(parse_and_evaluate(sample_string_3, sample_string_4))
    print(parse_and_evaluate(sample_string_5, sample_string_1))