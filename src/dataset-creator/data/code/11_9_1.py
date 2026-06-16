import sys
def check_segment(arr):
    return all(x == arr[0] for x in arr) if len(arr) > 0 else True
if __name__ == '__main__':
    sample_data = [1, 2, 3], [5, 5, 5], [], ['a', 'b'], ['x']
    results = []
    for segment in sample_data:
        is_equal_segment = check_segment(segment)
        flag = "EQUAL" if is_equal_segment else "MIXED"
        results.append(f"{segment} -> {flag}")
    print("\n".join(results))