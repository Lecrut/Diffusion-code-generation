LARGE_THRESHOLD = 100

def get_max_of_three(v_one, v_two, v_three):
    candidates = (v_one, v_two, v_three)
    max_val = None
    for cand in candidates:
        if max_val is None or cand > max_val:
            max_val = cand
    return max_val

if __name__ == '__main__':
    num_a = 45
    num_b = 120
    num_c = 78
    maximum = get_max_of_three(num_a, num_b, num_c)
    print(maximum)