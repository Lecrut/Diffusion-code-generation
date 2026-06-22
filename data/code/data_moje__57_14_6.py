FIB_COUNT=15
def build_fibonacci_sequence(count):
    if count <= 0:
        return []
    if count == 1:
        return [0]
    if count == 2:
        return [0, 1]
    prev_list = build_fibonacci_sequence(count - 1)
    return prev_list + [prev_list[-1] + prev_list[-2]]
if __name__ == '__main__':
    print(build_fibonacci_sequence(FIB_COUNT))