import sys
def solve():
    data = sys.stdin.read().split()
    if len(data) < 4:
        return
    try:
        a = int(data[0])
        b = int(data[1])
        c = int(data[2])
        d = int(data[3])
    except ValueError:
        return
    list_a = [a, b]
    list_b = [c, d]
    sum_a = sum(list_a)
    sum_b = sum(list_b)
    print(f"List A: {list_a}, Sum A: {sum_a}")
    print(f"List B: {list_b}, Sum B: {sum_b}")
    if sum_a > sum_b:
        print(f"List A has the greater total sum ({sum_a} > {sum_b})")
    elif sum_b > sum_a:
        print(f"List B has the greater total sum ({sum_b} > {sum_a})")
    else:
        print(f"Both lists have equal total sums ({sum_a} = {sum_b})")
if __name__ == '__main__':
    sample_input = "10 20 3 4"
    sys.stdin = open(sys.stdin.fileno(), 'r')                                                                                 
    a_val = 10
    b_val = 20
    c_val = 3
    d_val = 4
    list_a = [a_val, b_val]
    list_b = [c_val, d_val]
    sum_a = sum(list_a)
    sum_b = sum(list_b)
    print(f"List A: {list_a}, Sum A: {sum_a}")
    print(f"List B: {list_b}, Sum B: {sum_b}")
    if sum_a > sum_b:
        print(f"List A has the greater total sum ({sum_a} > {sum_b})")
    elif sum_b > sum_a:
        print(f"List B has the greater total sum ({sum_b} > {sum_a})")
    else:
        print(f"Both lists have equal total sums ({sum_a} = {sum_b})")