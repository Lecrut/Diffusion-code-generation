import sys
def check_mutual_exclusivity(conditions):
    n = len(conditions)
    for i in range(n):
        for j in range(i + 1, n):
            if conditions[i] and conditions[j]:
                return False
    return True
def read_conditions(filename):
    try:
        with open(filename, 'r') as f:
            lines = f.readlines()
            conditions = []
            for line in lines:
                line = line.strip()
                if line:
                    conditions.append(line)
            return conditions
    except FileNotFoundError:
        return None
if __name__ == '__main__':
    sample_filename = "conditions.txt"
    sample_content = [
        "A",
        "B",
        "C",
        "D"
    ]
    try:
        with open(sample_filename, 'w') as f:
            for cond in sample_content:
                f.write(cond + "\n")
        conditions_to_check = read_conditions(sample_filename)
        if conditions_to_check is None:
            print("Error: Could not read the conditions file.")
        else:
            is_exclusive = check_mutual_exclusivity(conditions_to_check)
            print(f"Conditions read: {conditions_to_check}")
            if is_exclusive:
                print("Result: The conditions are mutually exclusive.")
            else:
                print("Result: The conditions are NOT mutually exclusive (at least two conditions are true simultaneously).")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")