SIDELINE_CONSTANT = 20

def compute_area(side):
    doubled = side * side
    return doubled

if __name__ == '__main__':
    current_side = SIDELINE_CONSTANT
    final_area = compute_area(current_side)
    print(final_area)