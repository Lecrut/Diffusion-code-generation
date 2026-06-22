import sys
INITIAL_VALUE = 10
INCREMENTAL_VALUE = 25

def compute_total(value1, value2):
    return value1 + value2
if __name__ == '__main__':
    sample_value1 = INITIAL_VALUE
    sample_value2 = INCREMENTAL_VALUE
    total_result = compute_total(sample_value1, sample_value2)
    sys.stdout.write(str(total_result))