SIX_MULTIPLIER = 6
RANGE_START = 1
RANGE_END = 11
SAMPLE_MULTIPLIER = 5

def generate_multiplication_table(base_value, start_index, end_index):
    table = {}
    current = start_index
    while current < end_index:
        table[current] = base_value * current
        current += 1
    return table

def get_single_multiplier_value(table_dict, key):
    return table_dict.get(key)

if __name__ == '__main__':
    full_table = generate_multiplication_table(SIX_MULTIPLIER, RANGE_START, RANGE_END)
    print(full_table)
    specific_result = get_single_multiplier_value(full_table, SAMPLE_MULTIPLIER)
    print(specific_result)