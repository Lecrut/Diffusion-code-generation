import numpy as np
THRESHOLD = 1e-09

def compare_two_simple_quantities_now_summary(a, b):
    summary = {'mean': (a + b) / 2, 'median': a if a < b else b, 'difference': abs(a - b)}
    return summary
if __name__ == '__main__':
    sample1 = compare_two_simple_quantities_now_summary(3.1415926535, 3.1415926536)
    print(f'Summary for 3.1415926535 and 3.1415926536: {sample1}')
    sample2 = compare_two_simple_quantities_now_summary(0.1 + 0.2, 0.3)
    print(f'Summary for (0.1 + 0.2) and 0.3: {sample2}')
    sample3 = compare_two_simple_quantities_now_summary(1.0, 0.9999999999999999)
    print(f'Summary for 1.0 and 0.9999999999999999: {sample3}')